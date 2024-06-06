#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command-line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const requestCharacter = (url, retries = 3) => {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err) {
        if (retries > 0) {
          resolve(requestCharacter(url, retries - 1));
        } else {
          reject(err);
        }
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

const getCharacters = async () => {
  try {
    const response = await new Promise((resolve, reject) => {
      request.get(apiUrl, (err, _, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    const charactersUrls = response.characters;

    if (!Array.isArray(charactersUrls)) {
      console.error('Invalid response format. "characters" is not an array.');
      process.exit(1);
    }

    const characterPromises = charactersUrls.map(characterUrl => {
      return requestCharacter(characterUrl);
    });

    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach(name => {
      console.log(name);
    });
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
};

getCharacters();
