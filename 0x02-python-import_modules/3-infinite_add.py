#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    le = sys.argv
    sum = 0

    for a in range(1, len(le)):
        sum = sum + int(le[a])
        print("{}".format(sum))
