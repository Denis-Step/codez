import Board from "../Board";
import React from "react";
import { connect } from "react-redux";
import { addWord, refreshState, clickWord } from "../redux/actions";

export default function FullBoard(props) {
  const mapStateToProps = (state, ownProps) => {
    console.log(ownProps);
    return {
      game_ID: ownProps.game_ID,
      words: state.words,
    };
  };

  const mapDispatchToProps = (dispatch) => ({
    addWord: (word) => dispatch(addWord(word)),
    refreshState: (game_ID) => dispatch(refreshState(game_ID)),
    clickWord: (word) => dispatch(clickWord(word)),
  });

  FullBoard = connect(mapStateToProps, mapDispatchToProps)(Board);

  return <FullBoard {...props} />;
}
