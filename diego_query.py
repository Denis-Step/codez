from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from diego import Word, User, GameHistory
engine = create_engine('sqlite:///db.db', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

#Query --> List --> Model

def create_word(word, word_id):
    session.add(Word(word=word, wordid=word_id))
    session.commit()
    return True

def create_user(id, name, email, password, gamesPlayed, gamesWon):
    session.add(User(id=id, name=name, email=email, password=password, gamesPlayed=gamesPlayed, gamesWon=gamesWon))
    session.commit()
    return True

def create_game_history(game_history_id, history, winners, when):
    session.add(GameHistory(gamehistoryid=game_history_id, history=history, winners=winners, when=when))
    session.commit()
    return True

def read_word(word_read):
    q = session.query(Word).filter(Word.word==word_read)
    result = q.value('wordid')
    return {
    "word" : word_read,
    "wordid" : result
    }

def read_user(user_id):
    q = session.query(User).filter(User.id==user_id)
    user_dict = dict()
    user_dict["id"] = user_id
    fields = ["name", "email", "password", "gamesPlayed", "gamesWon"]
    for field in fields:
        user_dict[field] = q.value(field)
    return user_dict

def read_game_history(game_id):
    q = session.query(GameHistory).filter(GameHistory.gamehistoryid==game_id)
    game_dict = dict()
    game_dict["game history id"] = game_id
    fields = ["history", "winners", "when"]
    for field in fields:
        game_dict[field] = q.value(field)
    return game_dict

create_game_history("battle", "event", "Blue", "April" )

print(read_game_history("battle"))
