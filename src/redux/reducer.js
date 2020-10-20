import { ADD_WORD } from "./actionTypes";

const initialState = {
  words: ["hello", "malarkey", "baloney"],
};

export function clickApp(state = initialState, action) {
  switch (action.type) {
    case ADD_WORD:
      return Object.assign({}, state, {
        words: [...state.words, action.word],
      });
    default:
      return state;
  }
}
