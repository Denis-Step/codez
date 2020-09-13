import React, { Fragment, useContext } from "react";
import Cell from "./Cell";
import { BoardContext } from "./BoardContext";

export default function Board() {
  let ctxt = useContext(BoardContext);
  let words = Object.keys(ctxt.words);
  console.log("words are");
  console.log(ctxt.words);

  function handleClick(e) {
    console.log(e.target.id);
    console.log("clicked");
    ctxt.flipWord(e.target.id);
  }

  const cells = [];
  for (let i = 0; i < 25; i++) {
    const word = words[i];
    cells.push(
      <Cell
        key={words[i]}
        word={word}
        seen={ctxt.words[word]}
        onClick={handleClick}
      />
    );
  }
  //Hello

  return <div className={"board"}>{cells}</div>;
}
