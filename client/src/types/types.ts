
export type TEAM = "red" | "blue" | "neutral";
export type TURN = "chooser" | "spymaster"
export type CURR_TURN = "blue-spymaster" | "blue-chooser" | "red-spymaster" | "red-chooser";

export interface WordsState {
    [key: string]: "hidden" | "blue-revealed" | "red-revealed";
}

export interface PlayerState {
    attemptsLeft: number;
    bluePoints: number;
    redPoints: number;
    hint: string;
    turn: CURR_TURN;
    winner: TEAM | "none";
    words: WordsState;
}