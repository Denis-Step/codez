import React, { Fragment } from "react";
import Title from "./Title";
import { BoardContext, BoardContextProvider } from "./BoardContext";
import Board from "./Board";
import { loadWords } from "./apicalls";
import SpymasterBox from "./SpymasterBox";

export default function Game() {
  console.log(loadWords());
  return (
    <div className={"main"}>
      <Title />
      <BoardContextProvider>
        <SpymasterBox />
        <Board />
      </BoardContextProvider>
    </div>
  );
}
