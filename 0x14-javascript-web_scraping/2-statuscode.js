#!/usr/bin/node
const request = require('request');
const argv = process.argv;
request.get(argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
