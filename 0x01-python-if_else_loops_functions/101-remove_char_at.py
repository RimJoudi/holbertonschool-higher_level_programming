#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    if n < 0 or n > len(str):
        return str
    for x in str:
        if x != str[n]:
            str1 += x
    return str1
