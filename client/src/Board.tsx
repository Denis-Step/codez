import React, {useCallback} from "react";
import Cell from "./Cell";
import {clickWord, refreshState} from "./redux/actions";
import {useSelector, useDispatch} from "react-redux";

interface BoardProps {
  game_ID: string;
}


const Board = (props: BoardProps): JSX.Element => {
  const words = useSelector(state => state.words );
  console.log("These are the words");
  console.log(words);
  const dispatch = useDispatch();

  const handleClick = (word) => {
    dispatch(clickWord(props.game_ID, word));
  }
  
  if (words.length < 1) {
    console.log('empty');
    dispatch(refreshState(props.game_ID));
    return <></>
  }
  else {
    
    const cells: JSX.Element[] = [];
      
    for (const word in words) {
      cells.push(
        <Cell
          key={word}
          word={word}
          seen={words[word]}
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