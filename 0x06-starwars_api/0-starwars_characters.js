#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const charactersUrls = filmData.characters;

    if (!Array.isArray(charactersUrls)) {
      console.error('Invalid response format. "characters" is not an array.');
      return;
    }

    const characterPromises = charactersUrls.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (err, _, body) => {
          if (err) {
            reject(err);
          } else {
            try {
              resolve(JSON.parse(body).name);
            } catch (parseError) {
              reject(parseError);
            }
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => {
          console.log(name);
        });
      })
      .catch(err => {
        console.error('Error:', err);
      });
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
