#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const results = JSON.parse(body).results;
  let count = 0;
  for (const movie of results) {
    for (const character of movie.characters) {
      if (character.endsWith('/18/')) {
        count++;
        break;
      }
    }
  }
  console.log(count);
});
