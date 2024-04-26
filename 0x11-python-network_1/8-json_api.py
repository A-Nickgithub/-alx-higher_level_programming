#!/usr/bin/python3
"""Sends a POST request with a letter parameter to search for a user."""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
        payload = {'q': letter}
        url = 'http://0.0.0.0:5000/search_user'
        response = requests.post(url, data=payload)

        try:
            data = response.json()
            if data:
                print("[{}] {}".format(data.get('id'), data.get('name')))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
