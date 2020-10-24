import React from "react";
import Cell from "./Cell";

export default function Board(props) {
  console.log(props.words);

  function handleClick(e, word) {
    console.log(e.target.id);
    console.log("clicked");
    props.addWord(word);
  }

  const cells = [];
  for (let i = 0; i < 25; i++) {
    const word = props.words[i];
    cells.push(
      <Cell
        key={props.words[i]}
        word={word}
        onClick={(event) => {
          handleClick(event, props.words[i]);
        }}
      />
    );
  }
  //Hello

  return <div className={"board"}>{cells}</div>;
}
