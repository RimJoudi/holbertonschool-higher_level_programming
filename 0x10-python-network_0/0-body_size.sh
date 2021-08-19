#!/bin/bash
# takes in a URL sends a request to it, and displays the size of the body
curl -w '%{size_download}\n' -so /dev/null $1
