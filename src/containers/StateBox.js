import React, { Fragment, useContext } from "react";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core";

function StateBox(props) {
  let StateBox = () => {
    return (
      <div id="statebox">
        <Typography variant={h4}>{props.winner ? props.winner : ""}</Typography>
        <Typography variant={h4}>{props.turn}</Typography>
        <Typography variant={h4}>Red Score: {props.redPoints}</Typography>
        <Typography variant={h4}>Blue Score: {props.bluePoints}</Typography>
        <Typography variant={h4}>Hint: {props.hint}</Typography>
      </div>
    );
  };

  StateBox = connect(mapStateToProps)(StateBox);

  return <StateBox {...props} />;
}
