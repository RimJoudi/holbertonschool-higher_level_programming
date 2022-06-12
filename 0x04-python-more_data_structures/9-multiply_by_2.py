#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = dict()
    for i, j in a_dictionary.items():
        d[i] = j * 2
    return(d)
