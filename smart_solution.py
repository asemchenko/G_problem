#!/usr/bin/python2


def insert_zero(number):
    b_exp = get_big_exponent(number)
    return expand_number(number, b_exp)


def expand_number(number, b_exp):
    b_value = number // b_exp
    number -= b_exp * b_value
    number += b_exp * b_value * 10
    return number


def get_start_value(number):
    nine_amount = number // 9
    i = int(str(number % 9) + ('9' * nine_amount))
    return i


def find(little_exp, big_exp, number, n, should_expand=False):
    #print('[EXPAND] ' if should_expand else '', number)
    number_backup = number
    if number % n == 0:
        return number
    if little_exp == 0:
        return None
    if should_expand:
        expanded = expand_number(number, big_exp)
        r = find(little_exp * 10, big_exp * 10, expanded, n)
        if r:
            return r

    cur_little = (number // little_exp) % 10
    cur_big = (number // big_exp) % 10
    while cur_big < 9 and cur_little >= 1:
        cur_big += 1
        cur_little -= 1
        # updating number
        number = number - little_exp + big_exp
        #print('[LOOP] = ', number)
        # checking if number match conditions
        res = find(little_exp // 10, big_exp // 10, number, n)
        if res:
            return res
    res = find(little_exp // 10, big_exp // 10, number, n)
    if res:
        return res
    return find(little_exp, big_exp, number_backup, n, should_expand=True)


def get_big_exponent(number):
    return int(10 ** (len(str(number)) - 1))


def find_result(start_value, n):
    b_exp = get_big_exponent(start_value)
    l_exp = int(b_exp // 10)
    return find(l_exp, b_exp, start_value, n)


def find_final_result(n):
    if n < 10:
        return n
    cur = get_start_value(n)
    # tmp = n
    # while tmp % 10 == 0:
    #     cur *= 10
    #     tmp //= 10
    while True:
        r = find_result(cur, n)
        if r is not None:
            return r
        cur = insert_zero(cur)


# print find_final_result(int(input()))
for i in range(1, 76):
    print(i, ':', find_final_result(i))
