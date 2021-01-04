import fakeredis
import pytest
import exceptions
import random
import services


class TestGame:
    @classmethod
    # Shadow and Mock Redis Client
    def setup_class(cls):
        services.r = fakeredis.FakeStrictRedis()

    @pytest.fixture
    def bad_game_ID(self):
        return "DOESNT EXIST"

    @pytest.fixture
    def good_game_ID(self):
        return str(10000)

    @pytest.fixture
    def initial_word_states(self):
        return ("red", "blue", "bomb", "neutral")

    @pytest.fixture
    def turn_states(self):
        return ("blue-spymaster", "blue-chooser", "red-spymaster", "red-chooser")

    @pytest.fixture
    def spymaster_payload(self):
        return {"attempts": 3, "hint": "Test"}

    @pytest.mark.xfail(raises=exceptions.GameNotFoundError)
    def test_game_not_exists(self, bad_game_ID):
        services.get_state(bad_game_ID)

    def test_game_exists(self, good_game_ID, initial_word_states, turn_states):
        services.create_game(good_game_ID)
        state = services.get_state(good_game_ID)

        assert "wordsState" in state
        assert "playerState" in state

        for word in state["wordsState"]:
            print(state["wordsState"][word])
            assert state["wordsState"][word] in initial_word_states

        assert "winner" in state["playerState"]
        assert "turn" in state["playerState"]
        assert state["playerState"]["hint"] == ""
        assert state["playerState"]["attemptsLeft"] == "0"
        assert state["playerState"]["redPoints"] == "0"
        assert state["playerState"]["bluePoints"] == "0"
        assert state["playerState"]["turn"] in turn_states

    def test_spymaster_turn(self, good_game_ID, spymaster_payload):
        success = services.handle_turn(
            good_game_ID, "blue", "spymaster", spymaster_payload
        )
        assert success == 1
        pstate = services.get_state(good_game_ID)["playerState"]
        print(pstate)
        assert pstate["turn"] == "blue-chooser"
