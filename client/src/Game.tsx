import React from "react";
import { useRouteMatch } from "react-router-dom";
import Title from "./Title";
import Board from "./Board";
import StateBox from "./StateBox";
import HelperBox from "./HelperBox";
import {useDisclosure} from "@chakra-ui/react";

export interface MatchParams {
  id: string;
}

const Game = (): JSX.Element => {
  const match = useRouteMatch<MatchParams>("/play/:id") as {params: MatchParams};
  const { isOpen, onOpen, onClose } = useDisclosure();
  const game_ID = match.params.id;
  
  return (
    <div className={"main"}>
      <Title />
      <StateBox game_ID={game_ID} />
      <Board game_ID={game_ID} />
      <HelperBox />
    </div>
  );
}

export default Game;