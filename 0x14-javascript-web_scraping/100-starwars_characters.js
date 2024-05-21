#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (error, response, body) => {
  if (!error) {
    const film = JSON.parse(body);
    const charactersUrls = film.characters;
    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error(error);
        }
      });
    });
  } else {
    console.error(error);
  }
});
