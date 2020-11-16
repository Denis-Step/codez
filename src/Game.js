import React, { Fragment } from "react";
import Title from "./Title";
import FullBoard from "./containers/FullBoard";
import { loadWords } from "./apicalls";
import SpymasterBox from "./SpymasterBox";
import { useRouteMatch } from "react-router-dom";

export default function Game() {
  const game_ID = useRouteMatch("/:id").params.id;
  console.log(game_ID);
  return (
    <div className={"main"}>
      <Title />
      <SpymasterBox />
      <FullBoard game_ID={game_ID} />
    </div>
  );
}
