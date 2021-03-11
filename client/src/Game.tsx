import React from "react";
import Title from "./Title";
import Board from "./Board";
import { useRouteMatch } from "react-router-dom";

export interface MatchParams {
  id: string;
}

const Game = (): JSX.Element => {
  const match = useRouteMatch<MatchParams>("/:id") as {params: MatchParams};
  const game_ID = match.params.id;
  
  return (
    <div className={"main"}>
      <Title />
      <Board game_ID={game_ID} />
    </div>
  );
}

export default Game;