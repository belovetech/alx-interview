#!/usr/bin/node
/**
 * Starwars Characters
 */
const request = require('request');

movie_id = process.argv[2];
movie_url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request(movie_url, (err, res, body) => {
  if (err) console.log(err);
  let index = 0;
  characters = JSON.parse(body).characters;
  printMovieCharacter(characters, index);
});

let printMovieCharacter = function (url, i) {
  request(url[i], (err, res, body) => {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    if (++i < url.length) {
      printMovieCharacter(url, i++);
    }
  });
};
