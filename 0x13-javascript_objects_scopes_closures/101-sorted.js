#!/usr/bin/node

const { dict } = require('./101-data');

const result = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (occurrences in result) {
    result[occurrences].push(userId);
  } else {
    result[occurrences] = [userId];
  }
}

console.log(result);
