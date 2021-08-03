#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i;
  let k = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      k += 1;
    }
  }
  return k;
};
