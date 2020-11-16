import {
  ADD_WORD,
  RECEIVE_WORDS,
  CALL_WORDS,
  REVEAL_WORD,
} from "./actionTypes";
import { loadWords } from "../apicalls";

export function addWord(word) {
  return { type: ADD_WORD, word };
}

export function callingWords() {
  return { type: CALL_WORDS };
}

export function receiveWords(words) {
  const wordList = Object.getOwnPropertyNames(words);
  return { type: RECEIVE_WORDS, words: wordList };
}

export function fetchWords(game_ID) {
  return function (dispatch) {
    dispatch(callingWords());

    return loadWords(game_ID).then((data) => {
      console.log("Words loaded");

      dispatch(receiveWords(data.wordsState));
    });
  };
}

export function revealingWord() {
  return { type: REVEAL_WORD };
}

export function clickWord(word) {
  return function (dispatch) {
    dispatch(revealingWord());

    return loadWords().then((data) => {
      console.log("Refreshing after Click");

      dispatch(receiveWords(data.wordsState));
    });
  };
}
