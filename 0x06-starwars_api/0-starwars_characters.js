#!/usr/bin/env node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let people = [];
const names = [];

const requestCharacters = () => {
  return new Promise((resolve, reject) => {
    request(filmEndPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject(`Error: ${err} | StatusCode: ${res.statusCode}`);
      } else {
        const jsonBody = JSON.parse(body);
        people = jsonBody.characters;
        resolve();
      }
    });
  });
};

const requestNames = () => {
  const namePromises = people.map(p => {
    return new Promise((resolve, reject) => {
      request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          reject(`Error: ${err} | StatusCode: ${res.statusCode}`);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      });
    });
  });

  return Promise.all(namePromises);
};

const getCharNames = async () => {
  try {
    await requestCharacters();
    if (people.length > 0) {
      await requestNames();
      names.forEach((name, index) => {
        process.stdout.write(name + (index < names.length - 1 ? '\n' : ''));
      });
    } else {
      console.error('Error: Got no characters for some reason');
    }
  } catch (error) {
    console.error(error);
  }
};

getCharNames();
