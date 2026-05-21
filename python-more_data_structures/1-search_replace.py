#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    new = list(map(lambda i: replace if i == search else i, new))
    return new
