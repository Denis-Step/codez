import React from "react";
import Title from "./Title";
import StateBox from "./containers/StateBox";
import FullBoard from "./containers/FullBoard";
import { useRouteMatch } from "react-router-dom";

export interface MatchParams {
  id: string;
}

const Game = (): JSX.Element => {
  const match = useRouteMatch<MatchParams>("/:id")
  const game_ID = match?.params?.id;
  
  return (
    <div className={"main"}>
      <Title />
      <StateBox game_ID={game_ID} />
      <FullBoard game_ID={game_ID} />
    </div>
  );
}

export default Game;