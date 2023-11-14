#!/usr/bin/node
const factorial = (x) => {
  if (x < 0) {
    return (-1);
  } else if (x === 0 || isNaN(x)) {
    return (1);
  }
  return (x * factorial(x - 1));
};
console.log(factorial(Number(process.argv[2])));