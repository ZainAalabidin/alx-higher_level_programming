#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    films.forEach(film => {
      if (
        film.characters.includes(
          `https://swapi-api.alx-tools.com/api/people/${characterId}/`
        )
      ) {
        count++;
      }
    });

    console.log(count);
  }
});
