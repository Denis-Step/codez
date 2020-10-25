import { ADD_WORD, RECEIVE_WORDS } from "./actionTypes";
import { loadWords } from "../apicalls";

export function addWord(word) {
  return { type: ADD_WORD, word };
}

export function receiveWords(words) {
  console.log("in receive words");
  const wordList = Object.getOwnPropertyNames(words);
  console.log(wordList);
  return { type: RECEIVE_WORDS, words: wordList };
}

export function fetchWords() {
  // Thunk middleware knows how to handle functions.
  // It passes the dispatch method as an argument to the function,
  // thus making it able to dispatch actions itself.

  return function (dispatch) {
    // First dispatch: the app state is updated to inform
    // that the API call is starting.

    // dispatch(requestWords());

    // The function called by the thunk middleware can return a value,
    // that is passed on as the return value of the dispatch method.

    // In this case, we return a promise to wait for.
    // This is not required by thunk middleware, but it is convenient for us.

    return loadWords().then((data) => {
      console.log("Words loaded");
      // We can dispatch many times!
      // Here, we update the app state with the results of the API call.

      dispatch(receiveWords(data));
    });
  };
}
