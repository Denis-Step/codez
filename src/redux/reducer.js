import {
  ADD_WORD,
  RECEIVE_WORDS,
  CALL_WORDS,
  REVEAL_WORD,
  RECEIVE_GAME_STATE,
} from "./actionTypes";

const initialState = {
  winner: null,
  turn: "",
  attemptsLeft: 0,
  redPoints: 0,
  bluePoints: 0,
  words: {},
  hint: "",
  isFetching: false,
};

export function clickApp(state = initialState, action) {
  switch (action.type) {
    case ADD_WORD:
      return Object.assign({}, state, {
        words: [...state.words, action.word],
      });
    case RECEIVE_WORDS:
      console.log(action.words);
      return Object.assign({}, state, {
        words: action.words,
        isFetching: false,
      });
    case RECEIVE_GAME_STATE:
      console.log(action.gameInfo);
      return Object.assign({}, state, {
        winner: action.gameInfo.winner,
        turn: action.gameInfo.turn,
        attemptsLeft: action.gameInfo.attemptsLeft,
        redPoints: action.gameInfo.redPoints,
        bluePoints: action.gameInfo.bluePoints,
        hint: action.gameInfo.hint,
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
