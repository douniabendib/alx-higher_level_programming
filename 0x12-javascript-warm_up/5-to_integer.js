#!/usr/bin/node
const myCommand = process.argv[2];
const num = parseInt(myCommand);
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
