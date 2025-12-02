#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1 = (tuple_a + (0, 0))[:2]
    t2 = (tuple_b + (0, 0))[:2]
    sum_1 = t1[0] + t2[0]
    sum_2 = t1[1] + t2[1]
    return (sum_1, sum_2)
