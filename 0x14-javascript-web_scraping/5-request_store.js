#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (!error) {
    fs.writeFile(file, body, { encoding: 'utf-8' }, err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
