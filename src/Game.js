import React, { Fragment } from "react";
import Title from "./Title";
import StateBox from "./containers/StateBox";
import SpymasterBox from "./SpymasterBox";
import { useRouteMatch } from "react-router-dom";

export default function Game() {
  const game_ID = useRouteMatch("/:id").params.id;
  console.log("game_ID");
  return (
    <div className={"main"}>
      <Title />
      <StateBox />
      <FullBoard game_ID={game_ID} />
    </div>
  );
}
