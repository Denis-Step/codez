import React, {useCallback} from "react";
import Cell from "./Cell";
import {clickWord, refreshState} from "./redux/actions";
import {useSelector, useDispatch} from "react-redux";

interface BoardProps {
  game_ID: string;
}


const Board = (props: BoardProps): JSX.Element => {
  const words = useSelector(state => state.words );
  const dispatch = useDispatch();

  const handleClick = useCallback ( (word) => {
    dispatch(clickWord(props.game_ID, word));
    dispatch(refreshState(props.game_ID));
  },[dispatch])
  
  if (Object.getOwnPropertyNames(words.length < 1)) {
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