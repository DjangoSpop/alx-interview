#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <MovieID>');
  process.exit(1);
}

const getCharNames = async () => {
  try {
    request(filmEndPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error('Error:', err || `StatusCode: ${res.statusCode}`);
        return;
      }
      const filmData = JSON.parse(body);
      const characters = filmData.characters;

      if (!characters || characters.length === 0) {
        console.error('Error: Got no Characters for some reason');
        return;
      }

      const names = [];
      let count = 0;

      characters.forEach(characterUrl => {
        request(characterUrl, (err, res, body) => {
          if (err || res.statusCode !== 200) {
            console.error('Error:', err || `StatusCode: ${res.statusCode}`);
            return;
          }
          const characterData = JSON.parse(body);
          names.push(characterData.name);
          count++;
          if (count === characters.length) {
            names.forEach(name => console.log(name));
          }
        });
      });
    });
  } catch (error) {
    console.error('Error:', error);
  }
};

getCharNames();
