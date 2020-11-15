from nltk.corpus import wordnet as wn
import modelmethods as db
import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import random
from models import Word, User, GameHistory

engine = create_engine('sqlite:///db.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
r = redis.Redis(host='localhost', port=6379, db=0)

NUM_WORDS = 5757

# TODO: Make The Red/Blue/Neutral/Bomb Constants
def get_state(game_ID):
    '''Return player and word state'''
    state = {'playerState': r.hgetall('state:' + game_ID),
        'wordsState': r.hgetall('words:' + game_ID)}
    return state

def create_game(game_ID):
    '''Takes a UUID and creates two hashes, one for the player state
    and a second for the words. Throws an exception if either table
    cannot be created. Returns the dict of words. '''
    
    new_game = {'turn': 'blue-spymaster',
        'hint': '',
        'attemptsLeft': 0,
        'redPoints': 0,
        'bluePoints': 0}
    words = create_board()
    set_fields = r.hset('state:' + game_ID, mapping=new_game)
    set_fields += r.hset('words:' + game_ID, mapping=words)
    return {'playerState': new_game, 'wordsState': words} if set_fields == 30 else {}

# TODO: Refactor this!!
def create_board():
    session = Session()
    words = dict()

    Red, Blue, Neutral, Bomb = 0, 0, 0, 0
    i = 0
    while i < 25:
        n = random.randrange(5757)
        word = session.query(Word).filter(Word.wordid == n)
        word = word.value("word")
        if word in words:
            continue

        if Red < 9:
            words[word] = "red"
            Red += 1
            i += 1
        elif Blue < 8:
            words[word] = "blue"
            Blue += 1
            i += 1
        elif Neutral < 7:
            words[word] = "neutral"
            Neutral += 1
            i += 1
        elif Bomb < 1:
            words[word] = "bomb"
            Bomb += 1
            i += 1
    
    session.close()
    keys = list(words.keys())
    random.shuffle(keys)
    shuffledDict = dict()
    for key in keys:
        shuffledDict.update({key: words[key]})

    return words

def handle_turn(game_ID, team, action, payload):
    state = r.hgetall('state:' + game_ID)
    if f'{team}-{action}' != state[b'turn'].decode("utf-8"):
        print("Can't go now")
        return 0
    if action == 'spymaster':
        update = {b'hint': payload['hint'].encode()}
        if state[b'turn'].decode('utf-8').split("-")[0] == 'blue':
            update[b'turn'] = 'blue-chooser'
            update[b'attemptsLeft' ] = payload['attempts']
        else:
            update[b'turn'] = 'red-chooser'
            update[b'attemptsLeft'] = payload['attempts']
        r.hset('state:' + game_ID,mapping=update)

def lch(word_one, word_two):
    word_one = wn.synsets(word_one)[0]
    word_two = wn.synsets(word_two)[0]

    return word_one.lowest_common_hypernyms(word_two)
