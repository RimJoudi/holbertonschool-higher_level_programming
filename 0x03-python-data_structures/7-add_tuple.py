#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a or (0, 0)
    y = tuple_b or (0, 0)
    if len(tuple_a) == 1:
        x = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        y = (tuple_b[0], 0)
    return(x[0] + y[0], x[1] + y[1])
