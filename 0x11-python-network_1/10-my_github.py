#!/usr/bin/python3
"""takes my Github credentials (username and password) and uses the Github
API to display my id
"""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    response = get(url, auth=HTTPBasicAuth(username, password))
    try:
        obj = response.json()
        print(obj.get('id'))
    except ValueError:
        print(None)
