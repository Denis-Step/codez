import React, { CSSProperties, useState } from "react";
import { register } from "./apicalls";
import ReactDOM from "react-dom";
import {
  Box,
  VStack,
  FormControl,
  Square,
  Center,
  FormLabel,
  Input,
  Divider,
  Button,
  ChakraProvider,
  HStack,
} from "@chakra-ui/react";
import LoginButton from "./LoginButton";
import SignupButton from "./SignupButton";
interface SignupProps {}

const style_elTypewriterSignupButton = {
  borderRadius: "3.0px",
  filter: "drop-shadow(0.0px 2.0px 3px rgba(0, 0, 0, 0.3000))",
  overflow: "visible",
};
const style_elTypewriterLoginButton = {
  borderRadius: "3.0%",
  filter: "drop-shadow(0.0px 2.0px 3px rgba(0, 0, 0, 0.3000))",
  overflow: "visible",
};
const style_title: CSSProperties = {
  fontSize: 75,
  color: "black",
  textAlign: "center",
};

const style_SignIn: CSSProperties = {
  fontSize: 60,
  color: "black",
  textAlign: "center",
  display: "flex"
};

const SignupPage: React.FC = (props: SignupProps) => {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  return (
    <div
      className="login-grid-root login-background"
    >
      <div className="font-badlyStamped" style={style_title}>
        <span>CODEZ</span>
      </div>
      <Divider />
      <div className="font-n1942report ">
      <VStack>
        <span className="" style={style_SignIn}>
          Sign In
        </span>
        <FormControl>
          <VStack>
        <Input style={{width: '50%'}} size="lg" type="username" placeholder="Username" onChange={(e) => setName(e.currentTarget.value)} />
        <Input style={{width: '50%'}} size="lg" type="password" placeholder="password" onChange={(e) => setPassword(e.currentTarget.value)} />
        </VStack>
        </FormControl>
        
        <HStack>
        <Button size="lg" className="font-n1942report login-button">LOGIN </Button>
        <Button size="lg" className="font-n1942report signup-button">SIGNUP </Button>
        </HStack>
        </VStack>
        <Divider/>
      </div>

      <div>Row3</div>
    </div>
  );
};
ReactDOM.render(
  <ChakraProvider>
    <SignupPage />
  </ChakraProvider>,
  document.getElementById("root")
);
