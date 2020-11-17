import React from "react";
import axios from "axios";
import ReactDOM from "react-dom";
import Game from "./Game.js";

let BASE = "http://159.203.124.40:8000";

export async function get_State(game_ID) {
  let endpoint = `/${game_ID}/loadwords`;
  console.log(BASE + endpoint);

  const response = await axios({
    method: "get",
    url: BASE + endpoint,
    params: {},
  });

  console.log(response);
  const results = response.data;
  return results;
}

export async function revealWord(word) {
  let endpoint = "/api/revealword";
  let postData = { pick: word };
  console.log(postData);

  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: postData,
  });

  console.log(response);
  const results = response.data;
  return results;
}
