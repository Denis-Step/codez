import { createSlice } from "@reduxjs/toolkit";
import { clickApp } from "./reducer";

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

export const { increment, decrement, incrementByAmount } = wordslice.actions;
export default wordsSlice.reducer;
