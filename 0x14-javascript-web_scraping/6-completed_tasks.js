#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const completedTasks = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId]++;
      }
    });
    console.log(completedTasks);
  } else {
    console.error(error);
  }
});
