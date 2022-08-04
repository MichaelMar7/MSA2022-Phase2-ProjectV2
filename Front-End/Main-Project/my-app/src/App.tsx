import {useState} from 'react';
import './App.css';

function App() {
  const [input, setInput] = useState("");
  let searchMode = "Random";
  let quotes = undefined;
  return (
    <div>
      <h1> Anime Random Quotes Displayer </h1>
      <p>
          This is an React Typescript API application that displays random quotes from anime provided by the third party API <strong style={{color:"green"}}> AnimeChan </strong> created by <strong> rocktimsaikia </strong>. The url for the api is <a href="https://animechan.vercel.app/"> https://animechan.vercel.app/ </a>. 
      </p>
      <p>
        In API applicaiton allows the user to generate a <u> random anime quote from the API</u>, generate a random quote from a specific <u> Anime Title</u>, or generate a random quote from a specific <u> Anime Character</u>.
      </p>
      <div>
        <button onClick={random}>
        Random Anime Quote
        </button>
      </div>
      <div>
        <button onClick={animeTitle}>
        Anime Title
        </button>
      </div>
      <div>
        <button onClick={characterName}>
        Character Name
        </button>
      </div>
      <div>
        <label>Name</label><br/>
        <input type="text" onChange={e => setInput(e.target.value)}/><br/>
        <button onClick={search}>
        Anime Title
        </button>
      </div>

      <p> You are currently searching for {searchMode} </p>
      <p> You have entered {input} </p>
    </div>
  );

  function random() {
    searchMode = "Random";
  }

  function animeTitle() {
    searchMode = "animeTitle";
  }

  function characterName() {
    searchMode = "characterName";
  }

  function search(){
    if (searchMode === "Random") {
      fetch("https://animechan.vercel.app/api/random")
        .then(response => response.json())
        .then(quote => console.log(quote))
        
    } else if (searchMode === "animeTitle") {
      fetch("https://animechan.vercel.app/api/quotes/anime?title=" + input)
        .then(response => response.json())
        .then(quotes => console.log(quotes[Math.floor(Math.random() * quotes.length)]))
    } else if (searchMode === "characterName") {
      fetch("https://animechan.vercel.app/api/quotes/character?name=" + input)
        .then(response => response.json())
        .then(quotes => console.log(quotes[Math.floor(Math.random() * quotes.length)]))
    }
}
}

export default App;