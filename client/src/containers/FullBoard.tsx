import Board from "../Board";
import React from "react";
import { connect } from "react-redux";
import { addWord, refreshState, clickWord } from "../redux/actions";
import { get_State } from "../apicalls";

interface BoardState {
  words: Array<string>
}

const mapStateToProps = (state: BoardState, ownProps) => {
  return {
    game_ID: ownProps.game_ID,
    words: state.words,
  };
};

const mapDispatchToProps = (dispatch) => ({
  addWord: (word) => dispatch(addWord(word)),
  refreshState: (game_ID) => dispatch(refreshState(game_ID, get_State)),
  clickWord: (word) => dispatch(clickWord(word)),
});

export default connect(mapStateToProps, mapDispatchToProps)(Board);

