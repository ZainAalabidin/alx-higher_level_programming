#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

if (!apiUrl) {
    console.log("Usage: ./script.js <API_URL>");
    process.exit(1);
}

request(apiUrl, (err, response, body) => {
    if (err) {
        console.error(`An error occurred: ${err}`);
    } else if (response.statusCode !== 200) {
        console.error(`Failed to fetch data: ${response.statusCode}`);
    } else {
        const data = JSON.parse(body);
        const films = data.results;
        let count = 0;

        films.forEach(film => {
            if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
                count++;
            }
        });

        console.log(count);
    }
});
