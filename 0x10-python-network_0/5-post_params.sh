#!/bin/bash
#  script that takes in a URL, sends a POST request
curl "$1" -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD"
