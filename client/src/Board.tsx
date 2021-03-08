import React from "react";
import Cell from "./Cell";

interface BoardProps {
  game_ID: string;
  clickWord(word: string): void;
  refreshState(game_ID: string): void;
  words: any;
}

const Board = (props: BoardProps): JSX.Element => {

  function handleClick(word) {
    props.clickWord(word);
    props.refreshState(props.game_ID);
  }
  
  if (Object.getOwnPropertyNames(props.words).length < 1) {
    props.refreshState(props.game_ID);
    return <></>
  }
  else {
  
  const cells: any[] = [];
    
  for (const word in props.words) {
    cells.push(
      <Cell
        key={word}
        word={word}
        seen={props.words[word]}
        onClick={(event) => {
          handleClick(word);
        }}
      />
    );
  }

  return (<div className={"board"}>{cells}</div>);
}
}

export default Board