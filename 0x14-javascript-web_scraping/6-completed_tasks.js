#!/usr/bin/node
const request = require('request'); // Import the 'request' module for making HTTP requests.
const url = process.argv[2]; // Get the URL from the command line arguments.

request(url, (error, Response, body) => {
  // Make an HTTP GET request to the specified URL.
  if (!error) {
    const toDos = JSON.parse(body); // Parse the JSON response body into a JavaScript object.
    const completedTasks = {}; // Initialize an object to keep track of completed tasks by user ID.

    toDos.forEach(toDo => {
      // Iterate through each to-do item.
      if (toDo.completed) {
        // Check if the to-do item is completed.
        if (!completedTasks[toDo.userId]) {
          // If the user ID is not yet in the completed_tasks object,
          completedTasks[toDo.userId] = 0; // initialize it with a value of 0.
        }
        completedTasks[toDo.userId] += 1; // Increment the count of completed tasks for the user.
      }
    });
    console.log(completedTasks); // Log the completed tasks object to the console.
  }
});
