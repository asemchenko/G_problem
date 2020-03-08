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
        exp = self.endian_exp * 10
        num = self.number // exp
        while num % 10 == 9:
            num //= 10
            exp *= 10
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
        unfree_exp = littles_exp // 10
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

    def sophisticated_increase(self):
        # finding minimal digit position that can be increased
        exp = 1
        s = 0
        while (self.number // exp) % 10 == 9 or s == 0:
            s += (self.number // exp) % 10
            exp *= 10
        # building minimal number
        n = (self.number // exp) * exp
        n += exp
        s -= 1
        e = 1
        while s >= 9:
            n += e * 9
            e *= 10
            s -= 9
        n += e * s
        # updating number
        self.number = n

    def increment(self):
        if self.get_endian_digit() < 9 and self.get_little_digit() > 0:
            self.number += self.endian_exp - self.little_exp
            return self.number
        elif self.get_little_digit() == 0:
            self.sophisticated_increase()
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
        pass
    return i.get()


for j in range(1, 76):
    print(j, ':', find_answer(j))
