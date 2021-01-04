import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import store from "./redux/store";
import Game from "./Game.js";
import { Route, Switch } from "react-router";
import { BrowserRouter } from "react-router-dom";
import LoginPage from "./LoginPage";

ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path="/login">
        <LoginPage />
      </Route>
      <Route exact path="/:id">
        <Provider store={store}>
          <Game />
        </Provider>
      </Route>
    </Switch>
  </BrowserRouter>,
  document.getElementById("root")
);
