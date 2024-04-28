#!/bin/bash
# Using curl -w option to filter output
curl -s -o /dev/null -w "%{http_code}" "$1"
