#!/usr/bin/node

const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (error, response, body) => {
  if (!error) {
    const film = JSON.parse(body);
    const charactersUrls = film.characters;
    const promises = charactersUrls.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (!error) {
            const character = JSON.parse(body);
            resolve(character.name);
          } else {
            reject(error);
          }
        });
      });
    });
    Promise.all(promises).then((characters) => {
      console.log(characters.join('\n'));
    }).catch((error) => {
      console.error(error);
    });
  } else {
    console.error(error);
  }
});
