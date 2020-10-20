import { addWord } from "./actionTypes";

const initialState = {
  words: [],
};

function clickApp(state = initialState, action) {
  switch (action.type) {
    case ADD_WORD:
      const state = Object.assign({}, state, {
        words: [...state.words, action.word],
      });
      state.words.push(action.word);
      return state;
  }

  return state;
}
