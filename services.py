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


def create_game(game_ID, db=0):
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

        print(f'Adding word {word}')
        if Red < 9:
            words[word] = "Red"
            Red += 1
            i += 1
        elif Blue < 8:
            words[word] = "Blue"
            Blue += 1
            i += 1
        elif Neutral < 7:
            words[word] = "Neutral"
            Neutral += 1
            i += 1
        elif Bomb < 1:
            words[word] = "Bomb"
            Bomb += 1
            i += 1

    keys = list(words.keys())
    random.shuffle(keys)
    shuffledDict = dict()
    for key in keys:
        shuffledDict.update({key: words[key]})
    session.close()

    print(words)
    r.hmset(game_ID, words)
    return words


def lch(word_one, word_two):
    word_one = wn.synsets(word_one)[0]
    word_two = wn.synsets(word_two)[0]

    return word_one.lowest_common_hypernyms(word_two)
