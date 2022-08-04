import {useState} from 'react';
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
import TextField from "@mui/material/TextField";
import Button from '@mui/material/Button';
import './App.css';

function App() {
  const [input, setInput] = useState("");
  const [inputInfo, setInputInfo] = useState<undefined | any>(undefined);
  let searchMode = "Random";
  return (
    <div>
      <h1> Anime Random Quotes Displayer </h1>
      <p>
          This is an React Typescript API application that displays random quotes from anime provided by the third party API <strong style={{color:"green"}}> AnimeChan </strong> created by <strong> rocktimsaikia </strong>. The url for the api is <a href="https://animechan.vercel.app/"> https://animechan.vercel.app/ </a>. 
      </p>
      <p>
        In API applicaiton allows the user to generate a <u> random anime quote from the API</u>, generate a random quote from a specific <u> Anime Title</u>, or generate a random quote from a specific <u> Anime Character</u>.
      </p>

      <div style={{justifyContent: 'center'}}>
        <Button id={"searchModeButton"} onClick={random}> Random Anime Quote </Button>
        <Button id={"searchModeButton"} onClick={animeTitle}> Anime Title </Button>
        <Button id={"searchModeButton"} onClick={characterName}>Character Name </Button>
      </div>

      <div>
        <TextField
          id="search-bar"
          className="text"
          value={input}
          onChange={(e: any) => {
            setInput(e.target.value);
          }}
          label="Enter..."
          variant="outlined"
          placeholder="Search..."
          size="small"
        />
        <Button
            onClick={() => {
              search();
            }}
          >
            <SearchIcon style={{ fill: "blue" }} />
            GO
          </Button>
      </div>

      {inputInfo === undefined ? (
        <p> Error </p>
      ) : (
        <div>
          <p> 
            {inputInfo.anime}  <br/>
            {inputInfo.character} <br/>
            "{inputInfo.quote}"
            {inputInfo.anime === "Re:Zero kara Hajimeru Isekai Seikatsu" ? (
              <p> RE:ZERO! </p>
            ) : (
              <p></p>
            )}
          </p>
        </div>
      )}
    </div>
  );

  function random() {
    searchMode = "Random";
  }

  function animeTitle() {
    searchMode = "Anime Title";
  }

  function characterName() {
    searchMode = "Character Name";
  }

  function search(){
    if (searchMode === "Random") {
      fetch("https://animechan.vercel.app/api/random")
        .then(res => res.json())
        .then(quote => setInputInfo(quote))
      console.log("Random")

    } else if (searchMode === "Anime Title") {
      fetch("https://animechan.vercel.app/api/quotes/anime?title=" + input)
        .then(res => res.json())
        .then(quotes => setInputInfo(quotes[Math.floor(Math.random() * quotes.length)]))
      console.log("animeTitle")
    } else if (searchMode === "Character Name") {
      fetch("https://animechan.vercel.app/api/quotes/character?name=" + input)
        .then(res => res.json())
        .then(quotes => setInputInfo(quotes[Math.floor(Math.random() * quotes.length)]))
      console.log("characterName")
    }
}
}

export default App;