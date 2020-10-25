import { ADD_WORD, RECEIVE_WORDS } from "./actionTypes";

const initialState = {
  words: [],
};

export function clickApp(state = initialState, action) {
  switch (action.type) {
    case ADD_WORD:
      return Object.assign({}, state, {
        words: [...state.words, action.word],
      });
    case RECEIVE_WORDS:
      return Object.assign({}, state, {
        words: action.words,
      });
    default:
      return state;
  }
}
