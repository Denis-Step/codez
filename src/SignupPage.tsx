import React, { useState } from "react";
import { register } from "./apicalls";
import ReactDOM from "react-dom";
import {
  Box,
  HStack,
  FormControl,
  FormLabel,
  Input,
  Button,
  ChakraProvider
} from "@chakra-ui/react";

interface SignupProps {}

const SignupPage: React.FC = (props: SignupProps) => {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  return (
    <Box>
      <FormLabel>Input</FormLabel>
      <Input type="text" onChange={(e) => setName(e.target.value)} />
      <Input type="password" onChange={(e) => setPassword(e.target.value)} />
      <button
        onClick={(e) => {
          e.preventDefault();
          register(name, password);
        }}
      />
      <Button size="lg" border="2px" borderColor="green.500">Signup</Button>
    </Box>
  );
};
ReactDOM.render(
    <ChakraProvider><SignupPage /></ChakraProvider>, document.getElementById("root"));
