#!/bin/bash
#This script will receive a url from the cli and then use curl to display the size of the body of the response
# Send a GET request to the URL and pipe the response through sed to remove the headers, then count the characters in the body
curl -s "$1" | sed '/^\s*$/,$d' | wc -c
