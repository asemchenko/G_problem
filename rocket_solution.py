#! /usr/bin/python2


def get_start_value(number):
    nine_amount = number // 9
    i = int(str(number % 9) + ('9' * nine_amount))
    return i


class Number:
    def __init__(self, number):
        self.number = number
        # getting endian_exp
        self.endian_exp = 10  # self.calc_endian_exp()
        # init little_exp
        self.little_exp = 1

    def get_little_digit(self):
        return (self.number // self.little_exp) % 10

    def get_endian_digit(self):
        return (self.number // self.endian_exp) % 10

    def calc_endian_exp(self):
        return int(10 ** (len(str(self.number)) - 1))

    def find_littles_free_exp(self):
        exp = self.endian_exp
        num = self.number // self.endian_exp
        while num % 10 == 9:
            num //= 10
            exp *= 10
        # if in digit in last position == 0 => digit at endian exp can be smaller than 9 => exp will be equal to self.endian_exp
        # return exp * 10 if exp == self.endian_exp else exp
        return exp

    def find_biggest_unfree_exp(self):
        exp = self.endian_exp
        while (self.number // (exp * 10)) % 10 == 9:
            exp *= 10
        return exp

    def get_digit(self, exp):
        return (self.number // exp) % 10

    def carry_one(self):
        # carrying
        littles_exp = self.find_littles_free_exp()
        unfree_exp = self.find_biggest_unfree_exp()
        self.number += littles_exp
        # putting remained digits
        remain = self.get_digit(unfree_exp) - 1
        self.number -= unfree_exp * self.get_digit(unfree_exp)
        e = 1
        while remain:
            d = (self.number // e) % 10
            if d < 9:
                diff = min(9 - d, remain)
                self.number += e * diff
                remain -= diff
            e *= 10

    def increment(self):
        if self.get_endian_digit() < 9 and self.get_little_digit() > 0:
            self.number += self.endian_exp - self.little_exp
            return self.number
        # elif self.get_endian_digit() < 9 and self.get_little_digit() == 0:
        #     # TODO think should there be pass?
        #     pass
        else:
            self.carry_one()
        return self.get()

    def get(self):
        return self.number


def find_answer(n):
    if n < 10:
        return n
    start_value = get_start_value(n)
    if start_value % n == 0:
        return start_value
    i = Number(start_value)
    while i.increment() % n != 0:
        print('[TEMP] ', n, ';', i.get())
    return i.get()


for j in range(1, 100):
    print(j, ' : ', find_answer(j))
