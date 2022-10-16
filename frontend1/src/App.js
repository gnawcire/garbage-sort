import React, { useState, useEffect } from "react";
import ReactPlayer from 'react-player'

import './App.css';

function App() {
  
  const [data, setdata] = useState("");

  useEffect(() => {
    // Using fetch to fetch the api from 
    // flask server it will be redirected to proxy
    fetch("http://localhost:5000/background_process_test")
      .then((res) => res.text())
      .then((data) => {
            setdata(data)
            console.log(data)
            
            // Setting a data from api
        });
  }, []);
  

  function getResults() {
    fetch("http://localhost:5000/background_process_test")
    .then((res) => res.text())
    .then((data) => {
          setdata(data)
          console.log(data)
          
          // Setting a data from api
      });
    
      
  }
  return (
    
    <body>
    <div class="header">
            <div class="topnav">
                <a class="active" href="/">Home</a>
                <a href="game">Game</a>
                <a href="about">About</a>
            </div>
        </div>
    <div>
      <img src='http://localhost:5000/video' />
      <iframe src="https://giphy.com/embed/26gssIytJvy1b1THO" width="640" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/pbs-cute-animals-26gssIytJvy1b1THO"></a></p>
    <h1>{data}</h1>
    <button onClick={getResults}>
    Analyze!
    </button>
    </div>
    </body>
  );

    
  
}



export default App;
