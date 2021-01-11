import React, { Fragment, useContext } from "react";
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
      </form>
    </div>
  );
}
