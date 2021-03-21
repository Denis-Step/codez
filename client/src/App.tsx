import React from "react";
import { Provider } from "react-redux";
import store from "./redux/store";
import Routes from "./Routes";
import { ChakraProvider } from "@chakra-ui/react";
import { BrowserRouter } from "react-router-dom";

const App = (): JSX.Element => {

  return (
    <BrowserRouter>
      <Provider store={store}>
        <ChakraProvider>
          <Routes />
        </ChakraProvider>
      </Provider>
    </BrowserRouter>
  );
};

export default App;