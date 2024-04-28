#!/bin/bash
# Send a HEAD request to the URL and store the response headers in a variable
response_headers=$(curl -s -I "$1")

# Extract the status code from the response headers
status_code=$(echo "$response_headers" | head -n 1 | awk '{print $2}')

# Display the status code
echo "Status code: $status_code"