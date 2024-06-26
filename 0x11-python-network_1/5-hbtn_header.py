#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
