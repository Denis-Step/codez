import React, { useMemo } from "react";
import SpymasterBox from "./SpymasterBox";
import { Center, Text, Stack, HStack, VStack, Box } from "@chakra-ui/react";
import { useSelector } from "react-redux";

const StateBox = (props: {game_ID: string}): JSX.Element => {
  const gameState = useSelector((state) => {
    return {
      action: state.action,
      turn: state.turn,
      attemptsLeft: state.attemptsLeft,
      redPoints: state.redPoints,
      bluePoints: state.bluePoints,
      hint: state.hint,
      winner: state.winner
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
          {`${gameState.turn}'s Turn`}
        </Text>
        {gameState.action == "chooser" ? (
          <>
          <Text fontSize="md">Hint: {gameState.hint} </Text>
          <Text fontSize="md">Attempts Left: {gameState.attemptsLeft} </Text>
          </>
        ) : null}
      </VStack>
    ),
    [gameState]
  );
  
  // CHECK FOR WINNER
  if (gameState.winner != "none"){
    return (
      <Center>
        <Text fontSize="lg">{`${gameState.winner} WINS!!`}</Text>
        <hr style={{paddingBottom: "20px"}} />
      </Center>
    )
  }

  if (gameState.action == "chooser") {
    return (
      <Center>
        <Box w="50%">{PointsBox}</Box>
        <Box w="50%">{TurnBox}</Box>
      </Center>
    );
  } else {
    return (
      <Stack w="100%">
        <Center>
          <Box w="50%">{PointsBox}</Box>
          <Box w="50%">
            <VStack spacing={10}>
              {TurnBox}
              <SpymasterBox game_ID = {props.game_ID} />
            </VStack>
          </Box>
        </Center>
        <hr style={{paddingBottom: "20px"}} />
      </Stack>
    );
  }
};

export default StateBox;
