from sys import argv


def get_start_value(number):
    nine_amount = number // 9
    i = int(str(number % 9) + ('9' * nine_amount))
    # while i % number != 0:
    #     i += 1
    return i


def get_digit_sum(number):
    s = 0
    while number:
        s += number % 10
        number //= 10
    return s


def find_result(n):
    result = n
    while get_digit_sum(result) != n:
        result += n
    return result


for i in range(1, 100):
    print(i, ':', find_result(i))
