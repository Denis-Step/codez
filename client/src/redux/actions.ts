import {
  RECEIVE_TOKEN,
  ADD_WORD,
  RECEIVE_WORDS,
  CALL_WORDS,
  REVEAL_WORD,
  RECEIVE_GAME_STATE,
} from "./actionTypes";
import {PlayerState, WordsState} from "../types/types";
import {get_State, spymaster_Move, revealWord} from "../apicalls"

export function receiveToken(token: string): {type: typeof RECEIVE_TOKEN, token: string} {
  return {type: RECEIVE_TOKEN, 'token': token }
}

export function callingWords(): {type: typeof CALL_WORDS} {
  return { type: CALL_WORDS };
}

export function receiveGameState(gameInfo: PlayerState): {type: typeof RECEIVE_GAME_STATE, gameInfo: PlayerState } {
  return { type: RECEIVE_GAME_STATE, gameInfo: gameInfo };
}

export function receiveWordsState(words: WordsState): {type: typeof RECEIVE_WORDS, words: WordsState } {
  return { type: RECEIVE_WORDS, words: words };
}

export function refreshState(game_ID: string): (dispatch) => Promise<void> {
  console.log(game_ID);
  
  return function (dispatch) {
    dispatch(callingWords());

    return get_State(game_ID).then((data) => {
      dispatch(receiveGameState(data.playerState));
      dispatch(receiveWordsState(data.wordsState));
    });
  };
}

export function makeSpymasterMove(game_ID: string, hint: string, attempts: number): (dispatch) => Promise<void | ((dispatch) => void)> {
  return function(dispatch){
    dispatch(callingWords())
    
    return spymaster_Move(game_ID, hint, attempts).then((status) => {
      console.log(status);
      
      dispatch(refreshState(game_ID));
    })
  }
}

export function revealingWord(): {type: typeof REVEAL_WORD} {
  return { type: REVEAL_WORD };
}

export function clickWord(game_ID: string, word: string): (dispatch) => void {
  return async function (dispatch) {
    dispatch(revealingWord());
    const response = await revealWord(word);
    dispatch(refreshState(game_ID));
    
  };
}
