import React from "react";
import axios from "axios";
import ReactDOM from "react-dom";
import Game from "./Game.js";

let BASE = "http://127.0.0.1:5000/";

export async function loadWords() {
  let endpoint = "/api/loadwords";

  const response = await axios({
    method: "get",
    url: BASE + endpoint,
    params: {},
  });

  console.log(response);
  const results = Object.values(Object.values(response.data));
  return results;
}
