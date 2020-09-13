import React from "react";

export default function Cell(props) {
  let revealed = "";
  if (props.seen == false) {
    revealed = "cell not-revealed";
  } else {
    revealed = "cell " + props.seen;
  }

  return (
    <div id={props.word} onClick={props.onClick} className={revealed}>
      {props.word}
    </div>
  );
}
