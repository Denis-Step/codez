import axios from "axios";
import { WordsState, PlayerState } from "./types/types";

const BASE = "http://127.0.0.1:5000";

interface StateResponse {
  playerState: PlayerState;
  wordsState: WordsState;
}

export async function get_State(game_ID: string): Promise<StateResponse> {
  const endpoint = `/games/${game_ID}`;
  console.log(BASE + endpoint);

  const response = await axios({
    method: "get",
    url: BASE + endpoint,
    params: {},
  });

  const results = response.data;
  return results;
}

export async function spymaster_Move(
  game_ID: string,
  team: "red" | "blue",
  hint: string,
  attempts: number
): Promise<number> {
  const endpoint = `/games/${game_ID}`;

  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: {
      team: team,
      action: "spymaster",
      payload: { hint: hint, attempts: attempts },
    },
  });

  return response.status;
}

export async function reveal_Word(word: string): Promise<number> {
  const endpoint = "/api/revealword";

  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: { pick: word },
  });

  const results = response.data;
  return results;
}

export async function login(name: string, password: string): Promise<string> {
  const endpoint = "/auth";

  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: { username: name, password: password },
  });

  return response["access_token"];
}

export async function register(
  name: string,
  password: string
): Promise<number> {
  const endpoint = "/users";

  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: { action: "signup", username: name, password: password },
  });

  const results = response.status;
  return results;
}
