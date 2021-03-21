import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { words_reducer } from "./reducer";

const store = createStore(
  words_reducer,
  applyMiddleware(
    thunk 
  ) // lets us dispatch() functions
);
export default store;
