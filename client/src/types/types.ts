
export type Team = "red" | "blue" | "neutral";
export type Turn = "chooser" | "spymaster"
export type CurrTurn = "blue-spymaster" | "blue-chooser" | "red-spymaster" | "red-chooser";

export interface WordsState {
    [key: string]: "hidden" | "blue-revealed" | "red-revealed";
}

export interface PlayerState {
    attemptsLeft: number;
    bluePoints: number;
    redPoints: number;
    hint: string;
    turn: Turn;
    team: Team;
    winner: Team | "none";
}