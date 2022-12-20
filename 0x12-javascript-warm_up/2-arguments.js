#!/usr/bin/node
const arglen = process.argv.length;
if (arglen === 3) {
  console.log('Argument found');
} else if (arglen < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
