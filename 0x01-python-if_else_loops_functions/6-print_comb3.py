#!/usr/bin/python3
for i in range(0, 9):
    for x in range(i + 1, 10):
        if not(i == 8 and x == 9):
            print("{:d}{:d}".format(i, x), end=", ")
        else:
            print("{:d}{:d}".format(i, x), end="\n")
