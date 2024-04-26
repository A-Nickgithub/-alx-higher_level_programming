#!/usr/bin/node

function printArgument () {
  const arg = process.argv[2];
  if (arg === undefined) {
    console.log('No argument');
  } else {
    console.log(arg);
  }
}
printArgument();
