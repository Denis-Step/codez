import React, { Fragment, useContext } from "react";
import Cell from "./Cell";
import { BoardContext } from "./BoardContext";

export default function Board() {
  let ctxt = useContext(BoardContext);

  const cells = [];
  for (let i = 0; i < 25; i++) {
    cells.push(<Cell key={ctxt.words[i]} word={ctxt.words[i]} />);
  }
  //Hello

  return <div className={"board"}>{cells}</div>;
}
