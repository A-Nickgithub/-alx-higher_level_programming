#!/usr/bin/python3
def complex_delete(p, value):
    keys = [k for k in p if d[k] == value]
    for k in keys:
        p.pop(k)
        return p
