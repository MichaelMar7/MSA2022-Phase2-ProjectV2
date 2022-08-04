import {useState} from 'react';
import './App.css';

function App() {
  const [input, setInput] = useState("");
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
        <button onClick={search}>
        Random Anime Quote
        </button>
      </div>
      <div>
        <label>Name</label><br/>
        <input type="text" onChange={e => setInput(e.target.value)}/><br/>
        <button onClick={search}>
        Anime Title
        </button>
      </div>

      <p>
        You have entered {input}
      </p>
    </div>
  );

  function search(){
    alert("Search button has been clicked!");
}
}

export default App;