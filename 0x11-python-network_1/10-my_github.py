#!/usr/bin/python3
"""
This script takes my github credentials(username and password)
and uses github API to display my id
we must use Basic Authentication with PAT as password
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    json_resp = response.json()
    id = json_resp.get('id')
    print(id)
