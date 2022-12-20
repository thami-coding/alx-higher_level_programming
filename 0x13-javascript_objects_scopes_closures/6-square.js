#!/usr/bin/node

const Square = require('./5-square.js');
module.exports = class extends Square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let str = '';
    const size = this.size;
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < size; i++) {
      for (let j = 0; j < size; j++) {
        str += c;
      }
      console.log(str);
      str = '';
    }
  }
};
