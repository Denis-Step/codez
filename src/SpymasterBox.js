import React, { Fragment, useContext } from "react";
import Cell from "./Cell";
import { BoardContext } from "./BoardContext";
import TextField from "@material-ui/core/TextField";

export default function SpymasterBox() {
  return (
    <div id="spymasterbox">
      <form className={"spymasterBox"} noValidate autoComplete="off">
        <TextField
          id="outlined-basic"
          label="Spymaster Clue"
          variant="outlined"
        />
        <TextField
          id="outlined-basic"
          label="Spymaster Clue"
          variant="outlined"
        />
      </form>
    </div>
  );
}
