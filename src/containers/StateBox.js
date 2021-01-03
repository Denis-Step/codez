import React, { useState } from "react";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import { connect } from "react-redux";
import { makeSpymasterMove } from "../redux/actions";

export default function StateBox(props) {
  let StateBox = (props) => {
    const [attempts, setAttempts] = useState(0);
    const [hint, setHint] = useState("");

    const DecisionBox = (turn = props.turn) => {
      if (props.turn.split("-")[1] == "spymaster") {
        return (
          <div>
            <TextField
              id="outlined-basic-attempts"
              label="Attempts Left"
              variant="outlined"
              default={props.attemptsLeft}
              onChange={(e) => setAttempts(e.target.value)}
            />
            <TextField
              id="outlined-hint"
              label="Spymaster Hint"
              variant="outlined"
              default={props.hint}
              onChange={(e) => setHint(e.target.value)}
            />
            <Button
              variant="contained"
              onClick={(e) =>
                props.spymasterMove(props.game_ID, hint, attempts)
              }
            />
          </div>
        );
      } else {
        return (
          <div>
            <Typography variant="h5">
              Attempts Left: {props.attemptsLeft}
            </Typography>
            <Typography variant="h5">Hint: {props.hint}</Typography>
          </div>
        );
      }
    };

    return (
      <div id="statebox">
        <Typography variant="h4">
          {props.winner != "none" ? props.winner : ""}
        </Typography>
        <Typography variant="h4">{props.turn.split("-")[0]}</Typography>
        <Typography variant="h4">{props.turn.split("-")[1]}</Typography>
        <Typography variant="h4">Red Score: {props.redPoints}</Typography>
        <Typography variant="h4">Blue Score: {props.bluePoints}</Typography>
        <DecisionBox />
      </div>
    );
  };

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

  const mapDispatchToProps = (dispatch) => ({
    spymasterMove: (game_ID, hint, attempts) =>
      dispatch(makeSpymasterMove(game_ID, hint, attempts)),
  });

  StateBox = connect(mapStateToProps, mapDispatchToProps)(StateBox);

  return <StateBox {...props} />;
}
