#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = list(dict.fromkeys(my_list))
    sum = 0
    for i in unique:
        sum += i

    return sum
