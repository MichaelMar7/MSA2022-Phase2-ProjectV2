import axios from "axios";
import {useState} from 'react';
import './App.css';

function App() {
  const [playerTag, setPlayerTag] = useState("");
  const COC_API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc5ZmRjMDg1LTFhZDEtNGQ3Yy1hMGRhLThjMGQ4MWU1MjhlNiIsImlhdCI6MTY1OTI1MzYwNywic3ViIjoiZGV2ZWxvcGVyL2YwNDY0M2VlLTkyMTEtYTUyMi00ODkwLTUwYjZkNDc3M2I3MSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjIwMi4zNi4yNDQuMiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.vDUeh-XkAlK9DxtGJNBkPdmtfo0CEDbu6B8bOmSEtdGw4Cz8hthReRrMUyseXKySMEmK9n24Wchbs_rSnDZo8g"
  const config = {
    headers: {
      "Accept": "application/json",
      "Authorization": "Bearer " + COC_API_TOKEN
    }
  }
  const COC_BASE_API_URL = "https://api.clashofclans.com/v1";
  return (
    <div>
      <h1> Clash of Clans Player Search </h1>
      <div>
        <label> Player Tag </label><br/>
        <input type="text" id="player-tag" name="player-tag" onChange={e => setPlayerTag(e.target.value)}/><br/>
        <button onClick={search}> Search </button>
      </div>

      <p> You have entered {playerTag} </p>

      <div id="player-result">This will show the result</div>
    </div>
  );

  function search() {
    axios.get(COC_BASE_API_URL + "/players/#" + playerTag, {
      headers: {
        "Accept": "application/json",
        "Authorization": "Bearer " + COC_API_TOKEN
      }
    }).then((res) => {
      console.log(res.data);
    });
  }
}

export default App;