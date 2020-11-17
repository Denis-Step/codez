import {
  ADD_WORD,
  RECEIVE_WORDS,
  CALL_WORDS,
  REVEAL_WORD,
  RECEIVE_GAME_STATE,
} from "./actionTypes";
import { get_State } from "../apicalls";

export function addWord(word) {
  return { type: ADD_WORD, word };
}

export function callingWords() {
  return { type: CALL_WORDS };
}

export function receiveGameState(gameInfo) {
  return { type: RECEIVE_GAME_STATE, gameInfo: gameInfo };
}

export function receiveWordsState(words) {
  return { type: RECEIVE_WORDS, words: words };
}

export function refreshState(game_ID) {
  return function (dispatch) {
    dispatch(callingWords());

    return get_State(game_ID).then((data) => {
      console.log("Words loaded");

      dispatch(receiveGameState(data.playerState));
      dispatch(receiveWordsState(data.wordsState));
    });
  };
}

export function revealingWord() {
  return { type: REVEAL_WORD };
}

export function clickWord(word) {
  return function (dispatch) {
    dispatch(revealingWord());

    return get_State().then((data) => {
      console.log("Refreshing after Click");

      dispatch(receiveWordsState(data.wordsState));
    });
  };
}
