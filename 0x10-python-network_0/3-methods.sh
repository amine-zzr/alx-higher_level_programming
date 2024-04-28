#!/bin/bash
# Displays all HTTP methods the server will accept
curl -isX OPTIONS "$1" |awk '/Allow:/ {sub("Allow: ", ""); print}'
