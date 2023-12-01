#!/bin/bash
# script that sends a request to a URL
curl -s -o /dev/null -w "%{http_code}" "$1"
