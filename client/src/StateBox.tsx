import React, { useMemo } from "react";
import SpymasterBox from "./SpymasterBox";
import { Center, Text, Stack, VStack, Box } from "@chakra-ui/react";
import { useSelector } from "react-redux";
import HelperBox from "./HelperBox";

const StateBox = (props: { game_ID: string }): JSX.Element => {
  const gameState = useSelector((state) => {
    return {
      action: state.action,
      turn: state.turn,
      attemptsLeft: state.attemptsLeft,
      redPoints: state.redPoints,
      bluePoints: state.bluePoints,
      hint: state.hint,
      winner: state.winner,
    };
  });

  const PointsBox = useMemo(
    () => (
      <VStack spacing={10}>
        <Text color="red" fontSize="4xl">
          RED: {gameState.redPoints}{" "}
        </Text>
        <Text color="blue" fontSize="4xl">
          BLUE: {gameState.bluePoints}{" "}
        </Text>
      </VStack>
    ),
    [gameState.redPoints, gameState.bluePoints]
  );

  const TurnBox = useMemo(
    () => (
      <VStack spacing={10}>
        {gameState.action == "chooser" ? (
          <>
            <Text fontSize="lg">HINT: {gameState.hint} </Text>
            <Text fontSize="md">Attemps Left: {gameState.attemptsLeft} </Text>
          </>
        ) : (
          <SpymasterBox game_ID={props.game_ID} />
        )}
      </VStack>
    ),
    [gameState]
  );

  // CHECK FOR WINNER
  if (gameState.winner != "none") {
    return (
      <Center>
        <Text fontSize="lg">{`${gameState.winner} WINS!!`}</Text>
        <hr style={{ paddingBottom: "20px" }} />
      </Center>
    );
  }

  return (
    <Stack w="100%">
      <Center>
        <Box w="33%">{PointsBox}</Box>
        <Box w="33%">
          <Center>
            <VStack>
              <Text color={gameState.turn} fontSize="2xl">
                {`${gameState.turn}'s Turn`}
              </Text>
              <HelperBox />
            </VStack>
          </Center>
        </Box>
        <Box w="33%">{TurnBox}</Box>
      </Center>
      <hr style={{ paddingBottom: "20px" }} />
    </Stack>
  );
};

export default StateBox;
