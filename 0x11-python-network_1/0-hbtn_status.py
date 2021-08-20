#!/usr/bin/python3
"""
Python script that fetches
https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == '__main__':

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        html = response.read()
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
