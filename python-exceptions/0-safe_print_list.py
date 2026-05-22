#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print("".join("{}".format(my_list[i]) for i in range(x)))
        return x
        pass
    except Exception as e:
        raise e
