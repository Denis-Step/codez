import { createStore, applyMiddleware } from "redux";
import thunkMiddleware from "redux-thunk";
import { configureStore } from "@reduxjs/toolkit";
import { clickApp } from "./reducer";

const store = createStore(
  clickApp,
  applyMiddleware(
    thunkMiddleware // lets us dispatch() functions
  )
);
export default store;
