#!/usr/bin/node
const request = require("request");
const urlBase = "https://swapi-api.alx-tools.com/api/films/";
const movieId = process.argv[2];

const url = `${urlBase}${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    console.log(data.title);
  }
});
