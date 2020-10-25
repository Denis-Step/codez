import {
  ADD_WORD,
  RECEIVE_WORDS,
  CALL_WORDS,
  REVEAL_WORD,
} from "./actionTypes";

const initialState = {
  words: [],
  isFetching: false,
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
        isFetching: false,
      });
    case CALL_WORDS:
      return Object.assign({}, state, {
        isFetching: true,
      });
    case REVEAL_WORD:
      return Object.assign({}, state, {
        isFetching: true,
      });
    default:
      return state;
  }
}
