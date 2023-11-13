#!/usr/bin/node
const myCommand = process.argv[2];
const num = Number(myCommand);
if (myCommand === undefined || isNaN(myCommand)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
