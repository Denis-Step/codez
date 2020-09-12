from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import random
from diego import Word, User, GameHistory

class Game:

    def __init__(self):
        #Words: Red, Blue, Black, Bomb, + revealed at end
        self.words = self.create_word_dict()
        self.turn = "Red"
        self.teamHint = ""
        self.redPoints = 0
        self.bluePoints = 0
        self.winner = None

    def create_word_dict(self):
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
            print(f'{word} and ID {j}')

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

    def reveal_word(self,word):
        #Check for Bomb first:
        if self.words[word] == "Bomb":
            self.hint = ""
            self.set_winner('Red') if self.turn == "Blue" else self.set_winner("Blue")
        elif self.words[word] == "Red":
            self.words[word] = self.words[word] + "Revealed"
            self.redPoints += 1
            if self.turn == "Blue":
                self.change_turn()
        elif self.words[word] == "Blue":
            self.words[word] = self.words[word] + "Revealed"
            self.bluePoints += 1
            if self.turn == "Red":
                self.change_turn()
        elif self.words[word] == "Black":
            self.words[word] = self.words[word] + "Revealed"
            self.change_turn()
    
    def change_turn(self):
        if self.turn == "Red":
                self.turn = "Blue"
                self.hint = ""
        else:
            self.turn = "Red"
            self.hint = ""

    def make_turn(self,wordstoChoose,word):
        pass

    def set_winner(self,team):
        #TODO
        pass