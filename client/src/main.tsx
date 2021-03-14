import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import store from "./redux/store";
import Routes from "./Routes";
import { ChakraProvider } from "@chakra-ui/react";
import { BrowserRouter } from "react-router-dom";

ReactDOM.render(
  <BrowserRouter>
    <Provider store={store}>
      <ChakraProvider>
        <Routes />
      </ChakraProvider>
    </Provider>
  </BrowserRouter>,
  document.getElementById("root")
);
