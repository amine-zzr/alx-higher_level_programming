#!/usr/bin/python3

"""
Sends a POST request with the letter as a parameter.
Displays the id and name if the response body is properly JSON formatted
and not empty. Otherwise, displays an error message.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(
                        json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError: 
        print("Not a valid JSON")
