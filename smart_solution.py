#!/bin/python3
from sys import argv


def get_start_value(number):
    nine_amount = number // 9
    i = int(str(number % 9) + ('9' * nine_amount))
    return i


def find(little_exp, big_exp, number):
    number_backup = number

    cur_little = (number // little_exp) % 10
    cur_big = (number // big_exp) % 10
    while cur_big != 9:
        cur_big += 1
        cur_little -= 1
        # updating number
        number = number - little_exp + big_exp
        # checking if number match conditions
        if number % N == 0:
            return number
    # if no success
    number = number_backup
    cur_little = (number // little_exp) % 10
    cur_big = (number // big_exp) % 10



N = int(argv[1])
cur = get_start_value(N)
