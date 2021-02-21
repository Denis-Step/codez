import axios from "axios";

let BASE = "http://127.0.0.1:5000";

enum Word {
  "red",
  "blue",
  "neutral"
}

enum Turn {
  "blue-spymaster",
  "red-spymaster",
  "blue-chooser",
  "red-chooser"
}

interface GameState {
  attemptsLeft: Number,
  bluePoints: Number,
  redPoints: Number,
  turn: Turn,
  hint: String,
  winner: "red" | "blue" | "none"
}

interface WordsState {
  [index: string]: Word
}

interface StateResponse {
  playerState: GameState,
  wordsState: WordsState
}


export async function get_State(game_ID: string): Promise<StateResponse> {
  const endpoint = `/${game_ID}/loadwords`;
  console.log(BASE + endpoint);

  const response = await axios({
    method: "get",
    url: BASE + endpoint,
    params: {},
  });

  const results = response.data;
  return results;
}


export async function spymaster_Move(game_ID: string, hint: string, attempts: number): Promise<number> {
  const endpoint = `/${game_ID}/spymaster`
  console.log(hint)
  console.log(attempts)
  
  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: {hint: hint,
           attempts: attempts}
  })
  
  return response.status
}

export async function revealWord(word) {
  const endpoint = "/api/revealword";

  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: {pick: word},
  });

  const results = response.data;
  return results
}

export async function login(name: string, password: string): Promise<string> {
  const endpoint = "/auth";

  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: {username: name,
           password: password},
  });

  
  return response["access_token"]
}

export async function register(name: string, password: string): Promise<number> {
  const endpoint = "/users";

  const response = await axios({
    method: "post",
    url: BASE + endpoint,
    data: { action: "signup",
          username: name,
           password: password},
  });

  const results = response.status;
  return results
}