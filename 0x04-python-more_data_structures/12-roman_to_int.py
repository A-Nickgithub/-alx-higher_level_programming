#!/usr/bin/python3
def roman_to_int(roman_string):
    if not type(roman_string) is str or roman_string is None:
        return 0
    le = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    rev = roman_string[::-1]

    for n in range(len(rev)):
        k = rev[i]
        if n != 0 and le[rev[n - 1]] > le[k]:
            num -= le[k]
        else:
            num += le[k]
            return num
