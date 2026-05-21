#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1, t2 = tuple_a, tuple_b
    t1_len = len(t1)
    t2_len = len(t2)

    a_plus_b = tuple(((t1[i] if i < t1_len else 0) + (t2[i] if i < t2_len else 0))
                     for i in range(2))
    print("{}".format(a_plus_b))
