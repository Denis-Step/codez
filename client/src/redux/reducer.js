import {
  RECEIVE_TOKEN,
  ADD_WORD,
  RECEIVE_WORDS,
  CALL_WORDS,
  REVEAL_WORD,
  RECEIVE_GAME_STATE,
  AUTHENTICATED,
} from "./actionTypes";

const initialState = {
  auth: {
    authenticated: false,
    token: null,
  },
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
    case RECEIVE_TOKEN:
      return Object.assign({}, state, {
        auth: {
          authenticated: true,
          token: action.token,
        },
      });

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
