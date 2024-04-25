#!/bin/bash
#This script will receive a url from the cli and then use curl to display the size of the body of the response
curl -s "$1" | sed '/^\s*$/,$d' | wc -c
