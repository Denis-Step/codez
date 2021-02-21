import React, { Fragment } from "react";
import Title from "./Title";
import StateBox from "./containers/StateBox";
import FullBoard from "./containers/FullBoard";
import { useRouteMatch } from "react-router-dom";

const Game = (): JSX.Element => {
  const game_ID = useRouteMatch("/:id").params.id;
  return (
    <div className={"main"}>
      <Title />
      <StateBox game_ID={game_ID} />
      <FullBoard game_ID={game_ID} />
    </div>
  );
}

export default Game;