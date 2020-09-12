from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import random
from diego import Word, User, GameHistory

class Game:
    engine = create_engine('sqlite:///db.db', echo=True)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    def __init__(self):
        self.words = self.createWordDict()

    def createWordDict(self):
        engine = create_engine('sqlite:///db.db', echo=True)
        Base = declarative_base()
        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        session = Session()

        randdict = dict()

        Red, Blue, Black, Bomb = 0,0,0,0
        while len(randdict.keys()) < 25:

            j = random.randrange(5757)

            word = session.query(Word).filter(Word.wordid == j)
            word = word.value("word")

            if word not in randdict:
                if Red < 9:
                    randdict[word] = "Red"
                    Red += 1
                elif Blue < 8:
                    randdict[word] = "Blue"
                    Blue += 1
                elif Black < 7:
                    randdict[word] = "Black"
                    Black += 1
                elif Bomb < 1:
                    randdict[word] = "Bomb"
                    Bomb += 1

        keys = list(randdict.keys())
        random.shuffle(keys)
        shuffleddict = dict()
        for key in keys:
            shuffleddict.update({key:randdict[key]})
        session.close()
        return shuffleddict
        print(shuffleddict)
