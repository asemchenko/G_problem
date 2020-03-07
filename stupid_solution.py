from sys import argv

N = int(argv[1])


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


result = get_start_value(N)
while get_digit_sum(result) != N:
    print(result, ' : ', get_digit_sum(result))
    exit()
    result += N

print('[RESULT] = ', result)
