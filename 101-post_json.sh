#!/bin/bash

# Check if the correct number of arguments is provided
[ "$#" -ne 2 ] && { echo "Usage: $0 <URL> <JSON_FILE>"; exit 1; }

# Check if the JSON file exists
[ ! -f "$2" ] && { echo "Error: JSON file '$2' not found"; exit 1; }

# Send a POST request with the JSON file contents in the body and display the response body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
