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

def create_word(word, word_id):
    session.add(Word(word=word, wordid=word_id))
    session.commit()

def create_user(id, name, email, password, gamesPlayed, gamesWon):
    session.add(User(id=id, name=name, email=email, password=password, gamesPlayed=gamesPlayed, gamesWon=gamesWon))
    session.commit()

def create_game_history(game_history_id, history, winners, when):
    session.add(GameHistory(gamehistoryid=game_history_id, history=history, winners=winners, when=when))
    session.commit()
