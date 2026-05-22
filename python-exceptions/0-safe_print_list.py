#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print("".join("{}".format(my_list[i]) for i in range(x)))
        return x
        pass
    except Exception as e:
        raise e


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
