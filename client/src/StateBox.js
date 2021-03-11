import React, { useState } from "react";
import {Text} from "chakra-ui"
import { useSelector, useDispatch } from "react-redux";
import { makeSpymasterMove } from "./redux/actions";

const mapStateToProps = (state) => {
  return {
    winner: state.winner,
    turn: state.turn,
    attemptsLeft: state.attemptsLeft,
    redPoints: state.redPoints,
    bluePoints: state.bluePoints,
    hint: state.hint,
  };
};

const StateBox = (props) => {
    const gameInfo = useSelector ((state) => {return ({
      winner: state.winner,
      team: state.team,
      turn: state.turn,
      attemptsLeft: state.attemptsLeft,
      redPoints: state.redPoints,
      bluePoints: state.bluePoints,
      hint: state.hint,
    })});
    const [attempts, setAttempts] = useState(0);
    const [hint, setHint] = useState("");

    const DecisionBox = (turn = gameInfo.turn) => {
      if (gameInfo.turn == "spymaster") {
        return (
          <div>
            <input
              type="text"
              id="outlined-basic-attempts"
              label-text="Attempts Left"
              default={props.attemptsLeft}
              onChange={(e) => setAttempts(e.target.value)}
            />
            <input
              id="outlined-hint"
              label-text="Spymaster Hint"
              onChange={(e) => setHint(e.target.value)}
            />
            <button
              onClick={(e) =>
                props.spymasterMove(props.game_ID, hint, attempts)
              }
            />
          </div>
        );
      } else {
        return (
          <div>
            <p variant="h5">Attempts Left: {props.attemptsLeft}</p>
            <p variant="h5">Hint: {props.hint}</p>
          </div>
        );
      }
    };

    return (
      <div id="statebox">
        <p variant="h4">{props.winner != "none" ? props.winner : ""}</p>
        <p variant="h4">{props.turn.split("-")[0]}</p>
        <p variant="h4">{props.turn.split("-")[1]}</p>
        <p variant="h4">Red Score: {props.redPoints}</p>
        <p variant="h4">Blue Score: {props.bluePoints}</p>
        <DecisionBox />
      </div>
    );
  };



  const mapDispatchToProps = (dispatch) => ({
    spymasterMove: (game_ID, hint, attempts) =>
      dispatch(makeSpymasterMove(game_ID, hint, attempts)),
  });

export default StateBox;
