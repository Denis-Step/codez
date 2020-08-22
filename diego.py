from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///db.db', echo=True)

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

# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

# user = User(id=0, name='John', password='johnspassword')
# session.add(user)
# user1 = User(id=1, name='John', gamesWon=4)
# session.add(user1)

print(session)

# session.commit()
