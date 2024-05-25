#!/usr/bin/node

const fetch = require('node-fetch');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;

const getCharNames = async () => {
  try {
    const filmResponse = await fetch(filmEndPoint);
    const filmData = await filmResponse.json();

    if (!filmData.characters) {
      console.error('Error: Got no Characters for some reason');
      return;
    }

    const names = [];
    for (const characterUrl of filmData.characters) {
      const characterResponse = await fetch(characterUrl);
      const characterData = await characterResponse.json();
      names.push(characterData.name);
    }

    if (names.length > 0) {
      console.log('OK');
    } else {
      console.error('Error: No characters found');
    }
  } catch (error) {
    console.error('Error: ', error);
  }
};

getCharNames();
