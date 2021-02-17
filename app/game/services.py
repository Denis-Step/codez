import random
import redis
from game import exceptions
from models.models import Word


r = redis.Redis(host="localhost", port=6379, db=0)

NUM_WORDS = 5757
MAX_ATTEMPTS = 3

# TODO: Make The Red/Blue/Neutral/Bomb Constants


def encode_dict(state):
    new_state = dict()
    for k, v in state.items():
        if isinstance(v, str):
            new_state[k.encode()] = v.encode()
        elif isinstance(v, int):
            new_state[k.encode()] = v
    return new_state


def decode_dict(state):
    new_state = dict()
    for k, v in state.items():
        if isinstance(v, str):
            new_state[k.decode()] = v.decode()
        elif isinstance(v, int):
            new_state[k.decode()] = v
    return new_state


def get_state(game_ID: str) -> dict:
    """Return player and word state"""

    if r.exists("state:" + game_ID) == 0:
        raise exceptions.GameNotFoundError(message="Game not Found")

    state = {
        "playerState": decode_dict(r.hgetall("state:" + game_ID)),
        "wordsState": decode_dict(r.hgetall("words:" + game_ID)),
    }

    return state


def create_game(game_ID):
    """Takes a UUID and creates two hashes, one for the player state
    and a second for the words. Throws an exception if either table
    cannot be created. Returns the dict of words."""

    if r.exists("state:" + game_ID) == 1:
        raise Exception("Game exists already")

    new_game = {
        "winner": "none",
        "turn": "blue-spymaster",
        "hint": "",
        "attemptsLeft": 0,
        "redPoints": 0,
        "bluePoints": 0,
    }
    words = create_board()
    set_fields = r.hset("state:" + game_ID, mapping=new_game)
    set_fields += r.hset("words:" + game_ID, mapping=words)

    if set_fields == 31:
        return {"playerState": new_game, "wordsState": words}
    else:
        raise Exception("Could not make Game")


def create_board():
    words = dict()

    # Leave this logic but change to use parameters eventually instead of built-in constants.
    #
    Red, Blue, Neutral, Bomb = 0, 0, 0, 0
    i = 0
    while i < 25:
        n = random.randrange(5757)
        word = Word.query.filter_by(wordid=n)
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

    keys = list(words.keys())
    random.shuffle(keys)
    shuffled_dict = dict()
    for key in keys:
        shuffled_dict.update({key: words[key]})

    return shuffled_dict


def set_winner(game_ID, team, r=r):
    r.hset("state:" + game_ID, "winner", team)


def finish_turn(game_ID, team, r=r):
    opposite = "blue" if team == "red" else "red"
    state = r.hgetall("state:" + game_ID)
    if state[b"redPoints"] == 9:
        set_winner(game_ID, "red")
    elif state[b"bluePoints"] == 8:
        set_winner(game_ID, "blue")

    if int(state[b"attemptsLeft"]) == 0:
        update = {b"turn": opposite + "-" + "spymaster", b"hint": ""}
        r.hset("state:" + game_ID, mapping=update)
    return 1


def handle_turn(game_ID, team, action, payload, r=r):
    if action == "spymaster":
        update = {b"hint": payload["hint"].encode()}
        if team == "blue":
            update[b"turn"] = "blue-chooser"
            update[b"attemptsLeft"] = payload["attempts"]
        else:
            update[b"turn"] = "red-chooser"
            update[b"attemptsLeft"] = payload["attempts"]
        r.hset("state:" + game_ID, mapping=update)
        return 1
    elif action == "chooser":
        choose_word(game_ID, team, payload["choice"])
        return finish_turn(game_ID, team, r)


def spymaster_turn(game_ID, team, hint, attempts):
    update = {
        b"turn": f"{team}-chooser",
        b"hint": hint.encode(),
    }


def choose_word(game_ID, team, choice, r=r):
    opposite = "blue" if team == "red" else "red"
    if r.hget("words:" + game_ID, choice) == "bomb".encode():
        r.hset("words:" + game_ID, choice, "bomb-revealed-" + team)
        set_winner(game_ID, "red") if team == "blue" else set_winner(game_ID, "blue")

    elif r.hget("words:" + game_ID, choice) == team.encode():
        r.hincrby("state:" + game_ID, team + "Points", 1)
        r.hincrby("state:" + game_ID, "attemptsLeft", -1)
        r.hset("words:" + game_ID, choice, team + "-revealed")

    elif r.hget("words:" + game_ID, choice) == opposite.encode():
        r.hincrby("state:" + game_ID, opposite + "Points", 1)
        r.hset("state:" + game_ID, "attemptsLeft", 0)
        r.hset("words:" + game_ID, choice, opposite + "-revealed")

    elif r.hget("words:" + game_ID, choice) == b"neutral":
        print("Neutral")
        r.hset("state:" + game_ID, "attemptsLeft", 0)
        r.hset("words:" + game_ID, choice, "neutral" + "-revealed")
    else:
        r.hincrby("state:" + game_ID, "attemptsLeft", -1)


# TODO
"""def lch(word_one, word_two):
    word_one = wn.synsets(word_one)[0]
    word_two = wn.synsets(word_two)[0]

    return word_one.lowest_common_hypernyms(word_two)"""


# 495481 is the test case
