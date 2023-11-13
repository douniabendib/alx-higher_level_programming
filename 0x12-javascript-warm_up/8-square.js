#!/usr/bin/node
const command = process.argv[2];
const numOcc = Number(command);
if (command === undefined || isNaN(command)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numOcc; i++) {
	  console.log('X'.repeat(numOcc));
	  }
}
