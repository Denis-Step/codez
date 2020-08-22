from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Word(Base):
    __tablename__ = 'words'

    word = Column(String, primary_key=True)
    wordid = Column(Integer)

    def __repr__(self):
        return f'User {self.name}'

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    gamesPlayed = Column(Integer)
    gamesWon = Column(Integer)

    def __repr__(self):
        return f'User {self.name}'

class GameHistory(Base):
    __tablename__ = 'gamehistories'

    gamehistoryid = Column(String, primary_key=True)
    history = Column(String)
    winners = Column(String)
    when = Column(String)

    def __repr__(self):
        return f'User {self.name}'


user = User(id=1234, password='bakedbeans')
session.add(user)

print(user.password)
