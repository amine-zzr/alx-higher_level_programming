#!/usr/bin/node

const arg = process.argv[2];

if (!arg) {
  console.log('No arguments');
} else {
  console.log(arg);
}
