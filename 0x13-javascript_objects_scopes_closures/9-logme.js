#!/usr/bin/node
let i = 0;
exports.logMe = function (item) {
  console.log('%s: %s', i, item);
  i++;
};
