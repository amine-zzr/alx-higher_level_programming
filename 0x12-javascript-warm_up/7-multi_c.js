#!/usr/bin/node

let num = parseInt(process.argv[2], 10);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (num--) {
    console.log('C is fun');
  }
}
