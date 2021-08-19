#!/bin/bash
# send a request to a URL passed as an argument, and displays only the status code of the response.
curl $1 -sX POST -H "Content-Type: application/json" -d @$2
