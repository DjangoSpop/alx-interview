#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./0-starwars_characters.js [MovieID]');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    printCharacters(characters);
  } else {
    console.error(`Error: ${error || response.statusCode}`);
  }
});

function printCharacters(urls) {
  urls.forEach(function (url) {
    request(url, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body);
        console.log(character.name);
      }
    });
  });
}
