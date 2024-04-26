#!/usr/bin/python3
"""
This script will list the last 10 commits
made in a repository of a certain user. Both the
repository and the user are specified in the CLI.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repo> <owner>")
        sys.exit(1)

        repo = sys.argv[1]
        owner = sys.argv[2]

        url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: Unable to fetch commits. "
                  f"Status code: {response.status_code}")

            sys.exit(1)

        try:
            json_resp = response.json()
        except ValueError:
            print("Error: Invalid JSON response.")
            sys.exit(1)

        for commit in json_resp[:10]:
            commit_data = commit.get('commit')
            if commit_data:
                sha = commit_data.get('sha')
                author = commit_data.get('author', {}).get('name', "Unknown")
                print(f"{sha}: {author}")
            else:
                print("Error: Unable to parse commit data.")
