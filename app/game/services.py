import random
import redis
from game import exceptions
from models.models import Word


r = redis.Redis(host="localhost", port=6379, db=0)

NUM_WORDS = 5757
NUM_BLUE_WORDS = 8
NUM_RED_WORDS = 9
NUM_BOMB_WORDS = 1
MAX_ATTEMPTS = 3

# TODO: Add dunders to annotate private methods


class InvalidTurnError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ValidationError(Exception):
    """Unused for now, bubbling exceptions up the stack
    instead"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


def opposite(team):
    if team not in ("red", "blue"):
        raise Exception("Team must be red or blue")

    return "blue" if team == "red" else "red"


def encode_dict(state):
    new_state = dict()
    for k, v in state.items():
        if isinstance(v, str):
            new_state[k.encode()] = v.encode()
        elif isinstance(v, int):
            new_state[k.encode()] = v
    return new_state


def decode_dict(state):
    """Avoids a lot of annoying casts between int and str,
    and bytes and str. CHANGE AT YOUR OWN PERIL"""
    new_state = dict()
    for k, v in state.items():
        if v.decode().isnumeric():
            new_state[k.decode()] = int(v)
        else:
            new_state[k.decode()] = v.decode()
    return new_state


def get_state(game_ID: str) -> dict:
    """Return player and word state"""
    if r.exists("state:" + game_ID) == 0:
        raise exceptions.GameNotFoundError(message="Game not Found")

    state = {
        "playerState": decode_dict(r.hgetall("state:" + game_ID)),
        "wordsState": decode_dict(r.hgetall("words:" + game_ID)),
    }

    print(state["wordsState"])

    return state


def handle_turn(game_ID, team, action, payload):
    """Make sure Only Valid Moves Work"""

    state = get_state(game_ID)
    if state["playerState"]["winner"] != "none":
        return ["playerState"]
    if state["playerState"]["turn"] != team or state["playerState"]["action"] != action:
        raise InvalidTurnError(
            f'{state["playerState"]["action"]} for {state["playerState"]["turn"]} goes now'
        )
    if action == "spymaster":
        return spymaster_move(game_ID, payload["hint"], payload["attempts"])
    elif action == "chooser":
        return chooser_move(
            game_ID, state["wordsState"], payload["guess"], state["playerState"]["turn"]
        )


def create_game(game_ID):
    """Takes a UUID and creates two hashes, one for the player state
    and a second for the words. Throws an exception if either table
    cannot be created. Returns the dict of words."""

    if r.exists("state:" + game_ID) == 1:
        raise Exception("Game exists already")

    new_game = {
        "winner": "none",
        "turn": "blue",
        "action": "spymaster",
        "hint": "",
        "attemptsLeft": 0,
        "redPoints": 0,
        "bluePoints": 0,
    }
    words = create_board()
    set_fields = r.hset("state:" + game_ID, mapping=new_game)
    set_fields += r.hset("words:" + game_ID, mapping=words)

    if set_fields == 32:
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

        if Red < NUM_RED_WORDS:
            words[word] = "red"
            Red += 1
            i += 1
        elif Blue < NUM_BLUE_WORDS:
            words[word] = "blue"
            Blue += 1
            i += 1
        elif Neutral < 7:
            words[word] = "neutral"
            Neutral += 1
            i += 1
        elif Bomb < NUM_BOMB_WORDS:
            words[word] = "bomb"
            Bomb += 1
            i += 1

    keys = list(words.keys())
    random.shuffle(keys)
    shuffled_dict = dict()
    for key in keys:
        shuffled_dict.update({key: words[key]})

    return shuffled_dict


def spymaster_move(game_ID, hint, attempts):
    if attempts > MAX_ATTEMPTS:
        raise Exception("Cannot select more than 3 words")
    update = {"hint": hint, "attemptsLeft": attempts, "action": "chooser"}

    r.hset("state:" + game_ID, mapping=update)


def chooser_move(game_ID, words, guess, team):
    if words[guess] == "bomb":
        r.hincrby("state:" + game_ID, "attemptsLeft", -1)
        return set_winner(game_ID, opposite(team))

    elif words[guess] == team:
        r.hincrby("state:" + game_ID, team + "Points", 1)
        r.hincrby("state:" + game_ID, "attemptsLeft", -1)
        r.hset("words:" + game_ID, guess, team + "-revealed")

    elif words[guess] == opposite(team):
        r.hincrby("state:" + game_ID, opposite(team) + "Points", 1)
        r.hset("state:" + game_ID, "attemptsLeft", 0)
        r.hset("words:" + game_ID, guess, opposite(team) + "-revealed")

    elif words[guess] == "neutral":
        r.hset("state:" + game_ID, "attemptsLeft", 0)
        r.hset("words:" + game_ID, guess, opposite(team) + "-revealed")

    return finish_turn(game_ID)


def finish_turn(game_ID):
    """Return None or the winning team String"""
    state = get_state(game_ID)["playerState"]

    if state["redPoints"] == NUM_RED_WORDS:
        return set_winner(game_ID, "red")
    elif state["bluePoints"] == NUM_BLUE_WORDS:
        return set_winner(game_ID, "blue")

    if state["attemptsLeft"] == 0 and state["action"] == "chooser":
        r.hset(
            "state:" + game_ID,
            mapping={"turn": opposite(state["turn"]), "action": "spymaster"},
        )


def set_winner(game_ID, team):
    """Set Winner and if no exception, return winning team"""
    r.hset("state:" + game_ID, "winner", team)
    return team


# TODO
"""def lch(word_one, word_two):
    word_one = wn.synsets(word_one)[0]
    word_two = wn.synsets(word_two)[0]

    return word_one.lowest_common_hypernyms(word_two)"""


# 495481 is the test case
