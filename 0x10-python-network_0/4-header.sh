#!/bin/bash
#script that takes in a URL as an argument, sends a GET request
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1"
