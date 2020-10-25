import Board from "../Board";
import React from "react";
import { connect } from "react-redux";
import { addWord, fetchWords, clickWord } from "../redux/actions";

export default function FullBoard() {
  const mapStateToProps = (state) => {
    return {
      words: state.words,
    };
  };

  const mapDispatchToProps = (dispatch) => ({
    addWord: (word) => dispatch(addWord(word)),
    fetchWords: () => dispatch(fetchWords()),
    clickWord: (word) => dispatch(clickWord(word)),
  });

  FullBoard = connect(mapStateToProps, mapDispatchToProps)(Board);

  return <FullBoard />;
}
