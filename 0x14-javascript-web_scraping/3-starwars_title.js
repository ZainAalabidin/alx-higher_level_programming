#!/usr/bin/node
const request = require('request');
const urlBase = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];

const url = `${urlBase}${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
