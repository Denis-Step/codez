import React, { useState, useCallback } from "react";
import {
  VStack,
  Center,
  InputGroup,
  Input,
  Divider,
  Button,
  Text,
} from "@chakra-ui/react";
import { useHistory } from "react-router-dom";
import { create_Game, get_State } from "./apicalls";
import Title from "./Title";

const HomePage = (): JSX.Element => {
  const history = useHistory();
  const [createForm, setCreateForm] = useState("");
  const [chooseForm, setChooseForm] = useState("");

  const createGame = useCallback(async () => {
    if (createForm == "") {
      alert("No Game ID Selected");
    }
    const resp = await create_Game(createForm)
      .then((data) => {
        history.push(`play/${createForm}`);
      })
      .catch(() => {
        alert("Game ID Taken");
      });
  }, [createForm]);

  const chooseGame = useCallback(async () => {
    get_State(chooseForm)
      .then((data) => history.push(`play/${chooseForm}`))
      .catch(() => alert("Game not found"));
  }, [chooseForm]);

  return (
    <div>
      <Title />
      <Divider />
      <div>
        <VStack>
          <Text>Home Page</Text>
        </VStack>
        <Divider />
      </div>

      <Center>
        <VStack spacing={4}>
          <InputGroup size="lg">
            <Text>Create Game </Text>
            <Input
              placeholder="New GameID"
              onChange={(e) => setCreateForm(e.target.value)}
            />
            <Button
              size="lg"
              width={0.25}
              colorScheme="teal"
              variant="solid"
              onClick={createGame}
            >
              Submit
            </Button>
          </InputGroup>

          <InputGroup size="lg">
            <Text>Join Game </Text>
            <Input
              placeholder="Join "
              onChange={(e) => setChooseForm(e.target.value)}
            />
            <Button
              size="lg"
              width={0.25}
              colorScheme="teal"
              variant="solid"
              onClick={chooseGame}
            >
              Submit
            </Button>
          </InputGroup>
        </VStack>
      </Center>
    </div>
  );
};

export default HomePage;
