import React, { Fragment } from "react";
import Cell from "./Cell";

export default function Board() {
  const cells = [];

  for (let i = 0; i < 25; i++) {
    cells.push(<Cell key={i} />);
  }

  return <div class="board">{cells}</div>;
}
