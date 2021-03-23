import React from "react";
import GoogleButton from "react-google-button";
import { useHistory } from "react-router";

const SigninPage = (): JSX.Element => {
  const history = useHistory();

  const handleClick = (e) => {
    history.push("login");
  };

  return <GoogleButton onClick={handleClick} />;
};

export default SigninPage;
