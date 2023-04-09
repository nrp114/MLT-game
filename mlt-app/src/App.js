import React, {Component} from 'react';
import {
  BrowserRouter as Router,
  Route,
  Routes,
} from 'react-router-dom'

import QuestionView from "./components/QuestionView";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Router>
          <Routes>
            <Route path="/create" element={ <QuestionView/> } />
          </Routes>
        </Router>
      </div>
    );
  }
}

export default App;