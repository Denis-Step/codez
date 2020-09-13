import React, { Component } from "react";
import axios from "axios";
import { loadWords, revealWord } from "./apicalls";

let BoardContext = React.createContext();

class BoardContextProvider extends Component {
  constructor(props) {
    super(props);
    this.state = {
      words: {},
      flipWord: this.flipWord.bind(this),
    };
  }

  setBoard() {
    loadWords().then((result) => {
      this.setState({ words: result });
    });
  }

  flipWord(word) {
    revealWord(word).then((result) => {
      this.setBoard();
    });
  }

  componentDidMount() {
    this.setBoard();
  }

  render() {
    return (
      <BoardContext.Provider value={this.state}>
        {this.props.children}
      </BoardContext.Provider>
    );
  }
}

export { BoardContextProvider, BoardContext };
