#!/usr/bin/node
const x = process.argv[2];
let str = '';

if (parseInt(x)) {
  for (let i = 0; i < x; i++) {
    for (let i = 0; i < x; i++) {
      str += 'X';
    }
    console.log(str);
    str = '';
  }
} else {
  console.log('Missing number of occurrences');
}
