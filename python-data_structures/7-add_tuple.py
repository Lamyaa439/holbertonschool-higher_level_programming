#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Convert the tuple into a list
    t_a = tuple_a + (0, 0)
    t_b = tuple_b + (0, 0)
    sum_1 = t_a[0] + t_b[0]
    sum_2 = t_a[1] + t_b[1]
    return (sum_1, sum_2)
