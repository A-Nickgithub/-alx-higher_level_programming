#!/usr/bin/python3
def best_score(my_dictionary):
    if not my_dictionary:
        return None
    scores = list(my_dictionary.values())
    scores.sort()
    best = scores[-1]
    for k in my_dictionary:
        if my_dictionary[k] == best:
            return k
