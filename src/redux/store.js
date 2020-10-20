import { createStore } from "redux";
import { clickApp } from "./reducer";

export const store = createStore(clickApp);
