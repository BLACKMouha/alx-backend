#!/usr/bin/node
/* jshint esversion: 6 */

/**
 * Print all characters of a Star Wars movie
 * There is only one argument passed to the program and is the movie ID
 */
if (process.argv.length === 3) {
  const request = require('request');
  const id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

  request.get(url, function (e, r, b) {
    if (e) {
      throw (e);
    } else {
      for (const p of JSON.parse(b).characters) {
        request.get(p, function (x, t, y) {
          if (x) {
            throw (x);
          } else {
            console.log(JSON.parse(y).name);
          }
        });
      }
    }
  });
}
