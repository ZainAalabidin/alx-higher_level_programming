#!/bin/bash
# Variables for email and subject
email="test@gmail.com"
subject="I will always be here for PLD"
# Send a POST request to the URL with the specified variables and display the body of the response
curl -s -d "email=$email" -d "subject=$subject" "$1"
