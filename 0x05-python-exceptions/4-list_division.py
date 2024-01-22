#!/usr/bin/python3
def list_division(list1, list2, list_lenght):
    l3 = []
    for i in range(list_length):
        n = 0
        try:
            n = list1[i] / list2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("Out of range")
        except TypeError:
            print("Wrong type")
        finally:
            list3.append(n)
            return list3
