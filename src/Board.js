import React from "react";
import Cell from "./Cell";
import { connect } from "react-redux";

function Board(props) {
  console.log(props.words);

  function handleClick(e) {
    console.log(e.target.id);
    console.log("clicked");
  }

  const cells = [];
  for (let i = 0; i < 25; i++) {
    const word = props.words[i];
    cells.push(<Cell key={props.words[i]} word={word} onClick={handleClick} />);
  }
  //Hello

  return <div className={"board"}>{cells}</div>;
}

const mapStateToProps = (state) => {
  return {
    words: state.words,
  };
};

Board = connect(mapStateToProps)(Board);
export default Board;
