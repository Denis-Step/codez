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
