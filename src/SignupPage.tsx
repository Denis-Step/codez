import React, { useState } from "react";
import { register } from "./apicalls";
import ReactDOM from "react-dom";
import {
  Box,
  HStack,
  FormControl,
  Square,
  Center,
  FormLabel,
  Input,
  Button,
  ChakraProvider,
} from "@chakra-ui/react";

interface SignupProps {}

const SignupPage: React.FC = (props: SignupProps) => {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  return (
    <Center h={"100%"}>
        <Box
          style={{
            width: "300px",
            height: "100px",
            padding: "20px",
            position: "absolute",
          }}
          w={"100%"}
        >
          <FormLabel>Sign-in</FormLabel>
          <Input
            type="text"
            placeholder="Username"
            onChange={(e) => setName(e.target.value)}
          />
          <Input
            type="password"
            placeholder="Password"
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button
            size="lg"
            border="2px"
            borderColor="green.500"
            onClick={(e) => {
              e.preventDefault();
              register(name, password);
            }}
          >
            Signup
          </Button>
        </Box>
      </Center>
  );
};
ReactDOM.render(
  <ChakraProvider>
    <SignupPage />
  </ChakraProvider>,
  document.getElementById("root")
);
