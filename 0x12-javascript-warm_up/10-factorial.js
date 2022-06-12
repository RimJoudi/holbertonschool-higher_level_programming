#!/usr/bin/node
const n = Number(process.argv[2]);
function factorial (n) {
  if (n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}
