import React, { useMemo } from "react";
import {Center, Text, HStack, VStack, Box } from "@chakra-ui/react";
import { useSelector, useDispatch } from "react-redux";
import { makeSpymasterMove } from "./redux/actions";

const StateBox = (props: { game_ID: string }): JSX.Element => {
  const gameState = useSelector((state) => {
    return {
      action: state.action,
      turn: state.turn,
      attemptsLeft: state.attemptsLeft,
      redPoints: state.redPoints,
      bluePoints: state.bluePoints,
      hint: state.hint,
    };
  });

  const PointsBox = useMemo(
    () => (
      <VStack>
        <Text fontSize="lg">Red: {gameState.redPoints} </Text>
        <Text fontSize="lg">Blue: {gameState.bluePoints} </Text>
      </VStack>
    ),
    [gameState.redPoints, gameState.bluePoints]
  );

  const TurnBox = useMemo(
    () => (
      <VStack>
        <Text fontSize="md">
          Turn: {`${gameState.turn} ${gameState.action}`}
        </Text>
        {gameState.turn == "chooser" ? (
          <Text fontSize="md">Attempts Left: {gameState.attemptsLeft} </Text>
        ) : null}
      </VStack>
    ),
    [gameState]
  );

  return (
    <Center>
      <Box w='50%'>{PointsBox}</Box>
      <Box w='50%'>{TurnBox}</Box>
    </Center>
  );
};

export default StateBox;
