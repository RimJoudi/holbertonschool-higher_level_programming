#!/usr/bin/node
const fs = require('fs');
const fA = process.argv[2];
const fB = process.argv[3];
const fC = process.argv[4];
const readA = fs.readFileSync(fA, 'UTF8');
const readB = fs.readFileSync(fB, 'UTF8');
fs.appendFileSync(fC, readA + readB);
