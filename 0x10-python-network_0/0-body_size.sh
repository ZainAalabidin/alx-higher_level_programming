#!/bin/bash
<<<<<<< HEAD
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
=======
# send a request to an URL with curl, and displays the size of the body of the response
curl -s "$1" | wc -c
>>>>>>> be83247515eacd19dc1e219f58bafefff734676e
