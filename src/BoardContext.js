import React, { Component } from "react";
import axios from "axios";
import { loadWords } from "./apicalls";

let BoardContext = React.createContext();

class BoardContextProvider extends Component {
  constructor(props) {
    super(props);
    this.state = {
      words: {},
    };
  }

  setBoard() {
    loadWords().then((result) => {
      this.setState({ words: result });
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
