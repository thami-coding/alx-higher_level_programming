#!/usr/bin/node

const dict = require('./101-data.js').dict;

const values = Object.values(dict);
const newDict = {};

for (let i = 0; i < values.length; i++) {
  const array = [];
  let v = values[i];
  for (const [key, value] of Object.entries(dict)) {
    if (v === value) {
      array.push(key.toString());
    }
  }
  v = v.toString();
  newDict[v] = array;
}
console.log(newDict);
