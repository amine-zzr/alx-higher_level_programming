#!/usr/bin/python3

"""
Lists 10 commits of a repository by a user using the GitHub API.
"""

import requests
import sys


def list_commits(repo_name, owner_name):
    """Lists 10 most recent commits of a repository by a user."""
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get(
                    'commit', {}).get('author', {}).get('name')
            if sha and author_name:
                print(f"{sha}: {author_name}")
    else:
        print("Error fetching commits:", response.status_code)


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
