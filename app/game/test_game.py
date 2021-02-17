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
        encoded = services.encode_all(new_game)
        for k, v in encoded.items():
            assert isinstance(k, bytes)
            assert isinstance(v, (bytes, int))

    def test_game_not_exists(self, bad_game_ID):
        with pytest.raises(Exception) as excinfo:
            services.create_game(bad_game_ID)
            assert "Game exists already" in excinfo

    def test_create_board(self):
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
