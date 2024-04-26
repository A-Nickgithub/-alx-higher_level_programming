#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(parseInt(arg)) || parseInt(arg) < 1) {
  console.log('Missing size');
} else {
  const size = parseInt(arg);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
