from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import random
from models import Word, User, GameHistory

engine = create_engine("sqlite:///db.db", echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

# Query --> List --> Model


def check_if_exist(class_exist, object_exist):
    if class_exist == Word:
        q = session.query(Word).filter(Word.word == object_exist)
    elif class_exist == User:
        q = session.query(User).filter(User.id == object_exist)
    elif class_exist == GameHistory:
        q = session.query(GameHistory).filter(GameHistory.gamehistoryid == object_exist)
    if q.count() == 0:
        return False
    else:
        return True


def create_word(word, word_id):
    if check_if_exist(Word, word) == False:
        session.add(Word(word=word, wordid=word_id))
        session.commit()
    else:
        print("check_if_exist error")


def create_user(id, name, email, password, gamesPlayed, gamesWon):
    if check_if_exist(User, id) == False:
        session.add(
            User(
                id=id,
                name=name,
                email=email,
                password=password,
                gamesPlayed=gamesPlayed,
                gamesWon=gamesWon,
            )
        )
        session.commit()
    else:
        print("check_if_exist error")


def create_game_history(game_history_id, history, winners, date):
    if check_if_exist(GameHistory, game_history_id) == False:
        session.add(
            GameHistory(
                gamehistoryid=game_history_id,
                history=history,
                winners=winners,
                date=date,
            )
        )
        session.commit()
    else:
        print("check_if_exist error")


def read_word(word_read):
    q = session.query(Word).filter(Word.word == word_read)
    result = q.value("wordid")
    return {"word": word_read, "wordid": result}


def read_user(user_id):
    q = session.query(User).filter(User.id == user_id)
    user_dict = dict()
    user_dict["id"] = user_id
    fields = ["name", "email", "password", "gamesPlayed", "gamesWon"]
    for field in fields:
        user_dict[field] = q.value(field)
    return user_dict


def read_game_history(game_id):
    q = session.query(GameHistory).filter(GameHistory.gamehistoryid == game_id)
    game_dict = dict()
    game_dict["game history id"] = game_id
    fields = ["history", "winners", "date"]
    for field in fields:
        game_dict[field] = q.value(field)
    return game_dict


def update_word(word_update, wordid_update):
    if check_if_exist(Word, word_update):
        x = session.query(Word).get(word_update)
        x.wordid = wordid_update
        session.commit()
    else:
        print("update_word error")


def update_user(
    id_update,
    name_update,
    email_update,
    password_update,
    gamesPlayed_update,
    gamesWon_update,
):
    if check_if_exist(User, id_update):
        x = session.query(User).get(id_update)
        x.name = name_update
        x.email = email_update
        x.password = password_update
        x.gamesPlayed = gamesPlayed_update
        x.gamesWon = gamesWon_update
        session.commit()
    else:
        print("update_user error")


def update_game_history(
    game_history_id_update, history_update, winners_update, date_update
):
    if check_if_exist(GameHistory, game_history_id_update):
        x = session.query(GameHistory).get(game_history_id_update)
        x.game_history_id = game_history_id_update
        x.history = history_update
        x.winners = winners_update
        x.date = date_update
        session.commit()
    else:
        print("update_game_history error")


def delete_word(word_delete):
    if check_if_exist(Word, word_delete):
        x = session.query(Word).get(word_delete)
        session.delete(x)
        session.commit()
    else:
        print("delete_word error")


def delete_user(user_delete):
    if check_if_exist(User, user_delete):
        x = session.query(User).get(user_delete)
        session.delete(x)
        session.commit()
    else:
        print("delete_user error")


def delete_game_history(game_history_delete):
    if check_if_exist(GameHistory, game_history_delete):
        x = session.query(GameHistory).get(game_history_delete)
        session.delete(x)
        session.commit()
    else:
        print("delete_game_history error")
