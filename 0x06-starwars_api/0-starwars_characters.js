#!/usr/bin/env node

const fetch = require('node-fetch');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;

const getCharNames = async () => {
  try {
    const filmResponse = await fetch(filmEndPoint);
    const filmData = await filmResponse.json();

    if (!filmData.characters || filmData.characters.length === 0) {
      console.error('Error: Got no Characters for some reason');
      return;
    }

    const names = await Promise.all(filmData.characters.map(async (characterUrl) => {
      const characterResponse = await fetch(characterUrl);
      const characterData = await characterResponse.json();
      return characterData.name;
    }));

    if (names.length > 0) {
      console.log('OK');
      names.forEach(name => console.log(name));
    } else {
      console.error('Error: No characters found');
    }
  } catch (error) {
    console.error('Error: ', error);
  }
};

getCharNames();
