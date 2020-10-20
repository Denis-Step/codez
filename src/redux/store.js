import { createStore } from "redux";
import clickApp from "./reducer";

const store = createStore(todoApp);
console.log(store.getState());

store.dispatch(addWord("Hectic"));
