#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in range(len(my_string)):
        new_string += my_string[i] if my_string[i].lower() != "c" else ""
    return new_string
