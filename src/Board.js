import React from "react";
import Cell from "./Cell";

export default function Board(props) {
  if (Object.getOwnPropertyNames(props.words).length < 1) {
    props.refreshState(props.game_ID);
  }

  function handleClick(word) {
    props.clickWord(word);
  }

  const cells = [];
  for (const word in props.words) {
    cells.push(
      <Cell
        key={word}
        word={word}
        state={props.words[word]}
        onClick={(event) => {
          handleClick(word);
        }}
      />
    );
  }

  return <div className={"board"}>{cells}</div>;
}
