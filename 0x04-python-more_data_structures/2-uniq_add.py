#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.
    Args:
    my_list (list): A list of integers.
    Returns:
    int: The sum of all unique integers.
    """
    unique_sum = 0
    seen = set()

    for num in my_list:
        if num not in seen:
            unique_sum += num
            seen.add(num)

            return unique_sum

