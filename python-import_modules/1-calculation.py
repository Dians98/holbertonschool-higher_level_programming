#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    functions = [add, sub, mul, div]
    for func in functions:
        if func == add:
            operator = "+"
        elif func == sub:
            operator = "-"
        elif func == mul:
            operator = "*"
        elif func == div:
            operator = "/"
        print("{} {} {} = {}".format(a, operator, b, func(a, b)))
