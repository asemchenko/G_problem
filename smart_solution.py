#!/bin/python3
from sys import argv


def get_start_value(number):
    nine_amount = number // 9
    i = int(str(number % 9) + ('9' * nine_amount))
    return i


def find(little_exp, big_exp, number):
    if little_exp == 0:
        return None

    cur_little = (number // little_exp) % 10
    cur_big = (number // big_exp) % 10
    while cur_big < 9 and cur_little > 1:
        cur_big += 1
        cur_little -= 1
        # updating number
        number = number - little_exp + big_exp
        # checking if number match conditions
        if number % N == 0:
            return number
        res = find(little_exp // 10, big_exp // 10, number)
        if res is None:
            continue
        return res


N = int(argv[1])
cur = get_start_value(N)


def find_result(start_value):
    b_exp = int(10 ** (len(str(start_value)) - 1))
    l_exp = int(b_exp / 10)
    return find(l_exp, b_exp, start_value)


r = find_result(cur)
if r is None:
    r = find_result(cur * 10)
print(r)
