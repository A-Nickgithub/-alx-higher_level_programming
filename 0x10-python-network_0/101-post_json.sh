#!/bin/bash
# sends a JSON POST request to the URL passed and displays body of message
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
