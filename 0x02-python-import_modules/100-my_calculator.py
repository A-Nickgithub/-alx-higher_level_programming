#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    ops = ["+", "-", "*", "/"]
    le = sys.argv
    if len(le) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
        if not le[2] in ops:
            print("{}".format("Unknown operator. Available operators: +, -, * and /"))
            exit(1)
            a = int(le[1])
            b = int(le[3])
            op = le[2]
            result = (calc.add(a, b) if op == "+" else
                    calc.sub(a, b) if op == "-" else
                    calc.mul(a, b) if op == "*" else
                    calc.div(a, b) if op == "/" else 0)
            print("{} {} {} = {}".format(a, op, b, result))
