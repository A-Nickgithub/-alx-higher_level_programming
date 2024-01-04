#!/usr/bin/python3
"""
this program imports the functions from file calculator_1.py
it does not use the function print more than 4 times
has to define the following
value 10 to variable a
value 5 to variable b
the two varibles will only be used as arguments when calling print()
a and b must be defined on 2 different lines
it should call each of the imported function
it is not allowed to use * from importing or __import__
the code should not be executed when imported
"""
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_sub))
    print("{} * {} = {}".format(a, b, result_mul))
    print("{} / {} = {}".format(a, b, result_div))
