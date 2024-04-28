#!/bin/bash
# display all HTTP methods the server will accept using curl.
curl -s -I -X OPTIONS "$1" | grep -i '^allow:' | cut -d ' ' -f 2-
