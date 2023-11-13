#!/usr/bin/node
const myCommand = process.argv[2];
if (myCommand) {
  console.log(myCommand);
} else {
  console.log('No argument');
}
