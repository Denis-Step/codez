import React from "react";
import axios from "axios";
import ReactDOM from "react-dom";
import Game from "./Game.js";

let BASE = "http://127.0.0.1:5000";

export async function get_State(game_ID) {
  let endpoint = `/${game_ID}/loadwords`;
  console.log(BASE + endpoint);

  const response = await axios({
    method: "get",
    url: BASE + endpoint,
    params: {},
  });

  const results = response.data;
  return results;
}

export async function revealWord(word) {
  let endpoint = "/api/revealword";
  let postData = { pick: word };

  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: postData,
  });

  const results = response.data;
  return results;
}
