#! /usr/bin/python2
from interruptingcow import timeout


def get_exp(number):
    exp = 1
    while number % 10 == 0:
        exp *= 10
        number //= 10
    return exp


def get_start_value(number):
    nine_amount = number // 9
    i = int(str(number % 9) + ('9' * nine_amount))
    i *= get_exp(number)
    return i


class Number:
    def __init__(self, number, n):
        self.number = number
        # getting endian_exp
        self.endian_exp = 10  # self.calc_endian_exp()
        # init little_exp
        self.little_exp = 1
        # save n
        self.n = n
        self.n_exp = 1
        while (n % 10) == 0:
            n //= 10
            self.n_exp *= 10

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
        e = self.n_exp
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
    i = Number(start_value, n)
    while i.increment() % n != 0:
        pass
    return i.get()


db = {}
# print find_answer(int(input()))
r = [i for i in range(1, 1000)]
r.remove(165)
r.remove(185)
r.remove(275)
r.remove(297)
r.remove(308)
with open('db.txt', 'r') as f:
    # getting and removing already calculated
    for l in f.readlines():
        j = int(l.split(':')[0])
        r.remove(j)
total_skipped = 0
with open('db.txt', 'a') as f:
    for i in r:
        try:
            with timeout(45, exception=RuntimeError):
                print('Saving for ', i)
                db[i] = find_answer(i)
                f.write(str(i) + ':' + str(db[i]) + '\n')
                if i % 25 == 0:
                    f.flush()
        except RuntimeError:
            print('Timeout! Skipping')
            total_skipped += 1

print('Total skipped: ', total_skipped)
