#!/usr/bin/node

let num = parseInt(process.argv[2], 10);

if (!isNaN(num) && num > 0) {
  while (num--) {
    console.log('C is fun');
  }
} else if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
