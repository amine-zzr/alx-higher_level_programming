#!/bin/bash
# making a GET request and returning the size of the body
curl -s "$1" | wc -c
