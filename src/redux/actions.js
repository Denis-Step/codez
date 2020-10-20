import { ADD_WORD } from "./actionTypes";

export function addWord(word) {
  return { type: ADD_WORD, word };
}
