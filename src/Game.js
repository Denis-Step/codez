import React, { Fragment } from "react";
import Title from "./Title";
import { BoardContext, BoardContextProvider } from "./BoardContext";
import Board from "./Board";
import { loadWords } from "./apicalls";

export default function Game() {
  console.log(loadWords());
  return (
    <Fragment>
      <Title />
      Yerr
      <BoardContextProvider>
        <Board />
      </BoardContextProvider>
    </Fragment>
  );
}
