import React, { useState, useEffect, useRef } from 'react';
import io from 'socket.io-client';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'

function App() {
  const [questions, setQuestions] = useState(["Q1", "Q2", "Q3", "Q4", "Q4", "Q5", "Q6"]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [optionCount, setOptionCount] = useState([0, 0, 0, 0]); // initialize optionCount with default values

  const [options , setOptions ] = useState(["player1", "player2","player3","player4"])
  const socketRef = useRef(null);

  function handleNextQuestion(){
    setCurrentQuestion(currentQuestion + 1)
  }
  function handlePrevQuestion(){
    setCurrentQuestion(currentQuestion - 1)
  }

  const incrementOptionCount = (optionIdx) => {
    console.log(optionCount)
    const newOptionCount = [...optionCount]; // get the current option count from the state
    newOptionCount[optionIdx] += 1; // Increment the count for the selected option
    setOptionCount(newOptionCount); // update the state with the new option count
    console.log(newOptionCount)
    return newOptionCount
  }

  function handleOptionClick(optionIdx) {
    // Update the selected option state
    const newOptions = incrementOptionCount(optionIdx)
    sendOptionToServer(newOptions)
  }

  function sendOptionToServer(newOptions) {
    console.log(newOptions);
    socketRef.current.emit('newOptions', newOptions );
  }

  useEffect(() => {
    socketRef.current = io(); // create socket instance

    socketRef.current.on('connect', () => {
      console.log('Connected to server');
    });

    socketRef.current.on('optionReceive', (data) => {
      console.log('Received data from server:', data);
      setOptionCount(data.options)
    });

    return () => {
      socketRef.current.disconnect(); // disconnect socket on component unmount
    };
  }, []);

  return (
    <div>
      <div>
        Current Questions : {questions[currentQuestion]}
      </div>
      {
       options.map((option, index) => (
        <div  style={{ margin: '10px' }}>
        <button key={index}  onClick={() => handleOptionClick(index)} > Option {index + 1}: {option} : count {optionCount[index]}</button>
        </div>
       ))
      }
      <br></br>
      <button id="next_question" onClick={handleNextQuestion}> NEXT </button>
      <button id="prev_question" onClick={handlePrevQuestion}> PREV </button>
    </div> 
  );
}

export default App;
