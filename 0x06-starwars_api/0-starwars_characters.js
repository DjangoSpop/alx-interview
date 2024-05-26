const request = require('request');
const url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];
request(url, function(error, response, body) {
    if (error) {
        console.log(error);
    }
    else {
        let films = JSON.parse(body);
        let characters = films.characters;
        for (let index = 0; index < characters.length; index++) {
            request(characters[index], function(error, response, body) {
                if (error) {
                    console.log(error);
                }
                else {
                    let character = JSON.parse(body);
                    console.log(character.name);
                }
            });
        }
    }
});
