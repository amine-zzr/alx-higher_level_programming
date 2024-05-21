#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const ToWrite = process.argv[3];

fs.writeFile(filePath, ToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
