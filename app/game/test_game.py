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
            b"attemptsLeft": 0,
            b"redPoints": 0,
            b"bluePoints": 0,
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
        assert len([key for key, value in words.items() if value == "red"]) == 9
        assert len([key for key, value in words.items() if value == "blue"]) == 8
        assert len([key for key, value in words.items() if value == "bomb"]) == 1
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

    def test_set_winner(self, redis, good_game_ID):
        services.r = redis
        state = services.get_state(good_game_ID)
        print(state)
        assert "hint" in state["playerState"]
        assert state["playerState"]["winner"] == "none"

        services.set_winner(good_game_ID, "red")
        state = services.get_state(good_game_ID)
        assert state["playerState"]["winner"] == "red"
