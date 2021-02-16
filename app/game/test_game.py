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

    def test_game_not_exists(self, bad_game_ID):
        with pytest.raises(Exception) as excinfo:
            services.create_game(bad_game_ID)
            assert "Game exists already" in excinfo

    def test_game_exists(self, good_game_ID, initial_word_states, turn_states, redis):
        services.create_game(good_game_ID, r=redis)
        state = services.get_state(good_game_ID, r=redis)

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

    def test_spymaster_turn(self, good_game_ID, spymaster_payload, redis):
        success = services.handle_turn(
            good_game_ID, "blue", "spymaster", spymaster_payload, r=redis
        )
        assert success == 1
        pstate = services.get_state(good_game_ID, r=redis)["playerState"]
        assert pstate["turn"] == "blue-chooser"
        assert pstate["hint"] == spymaster_payload["hint"]
        assert pstate["attemptsLeft"] == str(spymaster_payload["attempts"])

    def test_chooser_turn(self, good_game_ID, redis):
        words_master = services.get_state(good_game_ID, r=redis)["wordsState"]
        blue_words = [word for word in words_master if "blue" in words_master[word]]
        assert len(blue_words) == 8

        for i in range(0, 3):
            payload = {"choice": blue_words[i]}
            services.handle_turn(good_game_ID, "blue", "chooser", payload, r=redis)

        new_state = services.get_state(good_game_ID, r=redis)["playerState"]
        assert new_state["turn"] == "red-spymaster"
        assert new_state["bluePoints"] == "3"
        assert new_state["redPoints"] == "0"
        assert new_state["attemptsLeft"] == "0"
        assert new_state["hint"] == ""
