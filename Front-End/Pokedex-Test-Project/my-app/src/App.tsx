import axios from "axios";
import { Pokemon } from "pokenode-ts";
import { useState } from 'react';
import './App.css';

function App() {
  const [pokemonName, setPokemonName] = useState("");
  const [pokemonInfo, setPokemonInfo] = useState<undefined | Pokemon>(undefined);

  const POKEMON_BASE_URL = "https://pokeapi.co/api/v2";
  return (
    <div>
      <h1> Pokemon Search </h1>

      <div>
        <label>Pokemon Name</label>
        <br />
        <input 
          type="text" 
          id="pokemon-name" 
          name="pokemon-name" 
          onChange={e => setPokemonName(e.target.value)}
        />
        <br />
        <button onClick={search}> Search </button>
      </div>

      <p> You have entered {pokemonName} </p>

      {pokemonInfo === undefined || pokemonInfo.sprites.other.dream_world.front_default === null ? (
        <p>Pokemon not found</p>
      ) : (
        <div id="pokemon-result">
          <img src={pokemonInfo.sprites.other.dream_world.front_default} />
          <p> ID: {pokemonInfo.id} </p>
          <p> Height: {pokemonInfo.height} </p>
          <p> Weight: {pokemonInfo.weight} </p>
        </div>
      )}
    </div>
  );

  function search(){
    axios.get(POKEMON_BASE_URL + "/pokemon/" + pokemonName).then((res) => {
      setPokemonInfo(res.data);
    });
  }
}

export default App;
