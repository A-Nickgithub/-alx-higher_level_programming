#!/usr/bin/python3
def multiple_returns(sentence):
    le = len(sentence)
    c = ""
    if le == 0:
        c = None
    else:
        c = sentence[0]
        return(le, c)
