#!/usr/bin/node

const commandArg = process.argv.slice(2).map(Number);

if (commandArg.length <= 1) {
  console.log(0);
} else {
  const sorted = commandArg.sort((a, b) => b - a);
  console.log(sorted[1]);
}
