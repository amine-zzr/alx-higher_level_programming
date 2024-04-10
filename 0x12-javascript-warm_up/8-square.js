#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

if (!isNaN(num) && num > 0) {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else if (isNaN(num)) {
  console.log('Missing size');
}
