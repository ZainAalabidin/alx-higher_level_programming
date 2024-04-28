#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response. no pipe
curl -s -I "$1" | head -n 1 | awk '{print $2}'
