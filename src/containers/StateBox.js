import React, { Fragment, useContext } from "react";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import { connect } from "react-redux";

export default function StateBox(props) {
  let StateBox = (props) => {
    return (
      <div id="statebox">
        <Typography variant="h4">
          {props.winner != "none" ? props.winner : ""}
        </Typography>
        <Typography variant="h4">{props.turn}</Typography>
        <Typography variant="h4">Red Score: {props.redPoints}</Typography>
        <Typography variant="h4">Blue Score: {props.bluePoints}</Typography>
        <Typography variant="h4">Hint: {props.hint}</Typography>
      </div>
    );
  };

  const mapStateToProps = (state) => {
    return {
      winner: state.winner,
      turn: state.turn,
      redPoints: state.redPoints,
      bluePoints: state.bluePoints,
      hint: state.hint,
    };
  };

  StateBox = connect(mapStateToProps)(StateBox);

  return <StateBox {...props} />;
}
