#!/usr/bin/node

const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

const contentA = fs.readFileSync(fileA);
const contentB = fs.readFileSync(fileB);
fs.writeFileSync(fileC, `${contentA}${contentB}`);
