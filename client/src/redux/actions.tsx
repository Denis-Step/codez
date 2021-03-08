import {
  RECEIVE_TOKEN,
  ADD_WORD,
  RECEIVE_WORDS,
  CALL_WORDS,
  REVEAL_WORD,
  RECEIVE_GAME_STATE,
  SPYMASTER_MOVE,
} from "./actionTypes";
import {get_State, spymaster_Move} from "../apicalls"

export function receiveToken(token){
  return {type: RECEIVE_TOKEN, 'token': token }
}

export function addWord(word) {
  return { type: ADD_WORD, word };
}

export function callingWords() {
  return { type: CALL_WORDS };
}

export function receiveGameState(gameInfo) {
  return { type: RECEIVE_GAME_STATE, gameInfo: gameInfo };
}

export function receiveWordsState(words) {
  return { type: RECEIVE_WORDS, words: words };
}

export function refreshState(game_ID, get_State) {
  console.log(game_ID);
  
  return function (dispatch) {
    dispatch(callingWords());

    return get_State(game_ID).then((data) => {
      console.log("Words loaded");

      dispatch(receiveGameState(data.playerState));
      dispatch(receiveWordsState(data.wordsState));
    });
  };
}

export function makeSpymasterMove(game_ID, hint, attempts){
  return function(dispatch){
    dispatch(callingWords())
    
    return spymaster_Move(game_ID, hint, attempts).then((status) => {
      console.log(status);
      
      return refreshState(game_ID, get_State)
    })
  }
}

export function revealingWord() {
  return { type: REVEAL_WORD };
}

export function clickWord(word) {
  return function (dispatch) {
    dispatch(revealingWord());
  };
}
