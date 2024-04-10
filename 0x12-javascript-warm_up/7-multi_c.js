#!/usr/bin/node

let num = parseInt(process.argv[2], 10);

if (num < 0) {
  return;
} else if (!isNaN(num) && num > 0) {
  while (num--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
