#!/usr/bin/node

const csquare = require('./5-square');

class Square extends csquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let k = '';
      for (let i = 0; i < this.width; i++) {
        k += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(k);
      }
    }
  }
}
module.exports = Square;
