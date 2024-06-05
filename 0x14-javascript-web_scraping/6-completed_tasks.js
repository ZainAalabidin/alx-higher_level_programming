#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, Response, body) => {
  if (error) {
    console.log(error);
  } else {
    const toDos = JSON.parse(body);
    const completed_tasks = {};

    toDos.forEach(toDo => {
      if (toDo.completed) {
        if (!completed_tasks[toDo.userId]) {
          completed_tasks[toDo.userId] = 0;
        }
        completed_tasks[toDo.userId]++;
      }
    });
    console.log(completed_tasks);
  }
});
