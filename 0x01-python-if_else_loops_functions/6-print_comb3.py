#!/usr/bin/python3

for i in range(0, 100, 1):
    f = int(i / 10)
    g = int(i % 10)
    if f == g:
        continue
    if f > g:
        continue
    if i == 89:
        print("{}{}".format(f, g))
        break
    print("{}{}, ".format(f, g), end="")
