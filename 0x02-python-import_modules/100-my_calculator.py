#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
args = len(sys.argv) - 1
if  args!= 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
if sys.argv[2] == '+':
    print("{}{}{} = {}".format(a, sys.argv[2], b, add(a,b)), end="\n")
elif sys.argv[2] == '-':
    print("{}{}{} = {}".format(a, sys.argv[2], b, sub(a,b)), end="\n")
elif sys.argv[2] == '*':
    print("{}{}{} = {}".format(a, sys.argv[2], b, mul(a,b)), end="\n")
elif sys.argv[2] == '/':
    print("{}{}{} = {}".format(a, sys.argv[2], b, div(a,b)), end="\n")
else:
    print("Unknown operator. Available operators: +, -, * and /", end="\n")
    exit(1)
