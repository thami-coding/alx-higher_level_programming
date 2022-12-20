#!/usr/bin/node
const num = process.argv[2];
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
if (parseInt(num)) {
  console.log(factorial(num));
} else {
  console.log(1);
}
