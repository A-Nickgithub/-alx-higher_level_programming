#!/bin/bash
# This script sends a request to the URL passed as an argument and displays only the status code of the response

# Send a GET request to the URL using curl, ignore the body output (-o /dev/null), and display only the HTTP response code (-w "%{http_code}")
curl -s -o /dev/null -w "%{http_code}" "$1"
