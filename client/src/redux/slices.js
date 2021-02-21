import { createSlice } from "@reduxjs/toolkit";

const initialState = { vords: [] };

const wordsSlice = createSlice({
  name: "words",
  initialState,
  reducers: {
    addWord(word) {
      state.words.push(word);
    },
    removeWord(word) {
      idx = state.words.indexOf(word);
    },
    incrementByAmount(state, action) {
      state.value += action.payload;
    },
  },
});

export const { increment, decrement, incrementByAmount } = wordsSlice.actions;
export default wordsSlice.reducer;
