import fakeredis
import pytest
import random
import services


class TestGame:
    @pytest.fixture
    def bad_game_ID(self):
        return "6003"

    @pytest.fixture
    def good_game_ID(self):
        return "92910"

    @pytest.fixture
    def initial_word_states(self):
        return ("red", "blue", "bomb", "neutral")

    @pytest.fixture
    def turn_states(self):
        return ("blue-spymaster", "blue-chooser", "red-spymaster", "red-chooser")

    @pytest.fixture
    def spymaster_payload(self):
        return {"attempts": 3, "hint": "Test"}

    def test_opposite(self):
        assert services.opposite("blue") == "red"
        assert services.opposite("red") == "blue"

        with pytest.raises(Exception) as excinfo:
            services.opposite("Red")
            assert "Could not make Game" in excinfo

    def test_encode_all(self):
        new_game = {
            "winner": "none",
            "turn": "blue-spymaster",
            "hint": "",
            "attemptsLeft": 0,
            "redPoints": 0,
            "bluePoints": 0,
        }
        encoded = services.encode_dict(new_game)
        for k, v in encoded.items():
            assert isinstance(k, bytes)
            assert isinstance(v, (bytes, int))

    def test_decode_all(self):
        new_game = {
            b"winner": b"none",
            b"turn": b"blue-spymaster",
            b"hint": b"",
            b"attemptsLeft": b"0",
            b"redPoints": b"0",
            b"bluePoints": b"0",
        }
        decoded = services.decode_dict(new_game)
        assert len(decoded) == 6
        for k, v in decoded.items():
            assert isinstance(k, str)
            assert isinstance(v, (str, int))

    def test_game_not_exists(self, bad_game_ID, redis):
        services.r = redis

        with pytest.raises(Exception) as excinfo:
            services.create_game(bad_game_ID)
            assert "Game exists already" in excinfo

    def test_create_board(self, redis):
        services.r = redis

        words = services.create_board()
        assert len(words.keys()) == 25
        assert (
            len([key for key, value in words.items() if value == "red"])
            == services.NUM_RED_WORDS
        )
        assert (
            len([key for key, value in words.items() if value == "blue"])
            == services.NUM_BLUE_WORDS
        )
        assert (
            len([key for key, value in words.items() if value == "bomb"])
            == services.NUM_BOMB_WORDS
        )
        assert len([key for key, value in words.items() if value == "neutral"]) == 7

    def test_create_game(self, redis, good_game_ID):
        services.r = redis

        game = services.create_game(good_game_ID)
        assert "playerState" in game
        assert "hint" in game["playerState"]

    def test_get_state(self, redis, good_game_ID):
        services.r = redis

        state = services.get_state(good_game_ID)
        assert "playerState" in state
        assert "wordsState" in state

    def test_spymaster_move(self, redis, good_game_ID):
        services.r = redis

        services.spymaster_move(good_game_ID, "test", 3)
        state = services.get_state(good_game_ID)
        assert state["playerState"]["turn"] == "blue"
        assert state["playerState"]["action"] == "chooser"
        assert state["playerState"]["hint"] == "test"

    def test_chooser_move(self, redis, good_game_ID):
        services.r = redis

        words = services.get_state(good_game_ID)["wordsState"]
        blueWords = [word for word in words if words[word] == "blue"]
        redWords = [word for word in words if words[word] == "red"]
        bombWords = [word for word in words if words[word] == "bomb"]

        # BLUE CHOOSES BLUE WORD
        services.chooser_move(good_game_ID, words, blueWords[0], "blue")
        updatedState = services.get_state(good_game_ID)
        assert updatedState["wordsState"][blueWords[0]] == "blue-revealed"
        assert updatedState["playerState"]["bluePoints"] == 1
        assert updatedState["playerState"]["attemptsLeft"] == 2

        # BLUE CHOOSES RED WORD
        services.chooser_move(good_game_ID, words, redWords[0], "blue")
        updatedState = services.get_state(good_game_ID)
        assert updatedState["wordsState"][redWords[0]] == "red-revealed"
        assert updatedState["playerState"]["bluePoints"] == 1
        assert updatedState["playerState"]["redPoints"] == 1
        assert updatedState["playerState"]["attemptsLeft"] == 0
        assert updatedState["playerState"]["turn"] == "red"
        assert updatedState["playerState"]["action"] == "spymaster"

        # RED CHOOSES BOMB
        services.spymaster_move(good_game_ID, "secondTest", 3)
        services.chooser_move(good_game_ID, words, bombWords[0], "red")
        updatedState = services.get_state(good_game_ID)
        assert updatedState["playerState"]["winner"] == "blue"

    def test_set_winner(self, redis, good_game_ID):
        services.r = redis
        state = services.get_state(good_game_ID)

        services.set_winner(good_game_ID, "red")
        state = services.get_state(good_game_ID)
        assert state["playerState"]["winner"] == "red"
