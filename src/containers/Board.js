import Board from "../Board";
import React from "react";
import { connect } from "react-redux";
import { addWord } from "../redux/actions";

export default function FullBoard() {
  const mapStateToProps = (state) => {
    return {
      words: state.words,
    };
  };

  const mapDispatchToProps = (dispatch) => ({
    addWord: (word) => dispatch(addWord(word)),
  });

  FullBoard = connect(mapStateToProps, mapDispatchToProps)(Board);

  return <FullBoard />;
}
