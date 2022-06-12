#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
