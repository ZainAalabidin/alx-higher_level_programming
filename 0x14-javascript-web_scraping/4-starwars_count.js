#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';
let count = 0;

request(apiUrl, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const films = data.results;
    

    films.forEach(film => {
      if (
        film.characters.includes(
          `https://swapi-api.alx-tools.com/api/people/${characterId}/`
        )
      ) {
        count++;
      }
    });
  }
  console.log(count);
});
