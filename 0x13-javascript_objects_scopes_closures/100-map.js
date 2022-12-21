#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((i, element) => i * element);
console.log(list);
console.log(newList);
