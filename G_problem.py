import math


def sum_digits(number):
    # number_str = str(number)
    # summa = 0
    # for digit in number_str:
    #     summa += int(digit)
    # return summa
    s = 0
    while number:
        s += number % 10
        number //= 10
    return s


def find_result(number):
    step = 9
    if number % 3 == 0:
        step = 3
    if number % 9 == 0:
        step = 1
    k = 1
    while True:
        testing_number = k * number
        if sum_digits(testing_number) == number:
            return testing_number
        k += step


def find_result_more_effective(number):
    step = 9
    if number % 3 == 0:
        step = 3
    if number % 9 == 0:
        step = 1
    testing_number = generate_min_number(number)
    testing_number = testing_number - testing_number % number
    k = int(testing_number / number)
    while (k % 9) != 1:
        k -= 1
    testing_number = k * number
    while True:
        print(testing_number)
        if sum_digits(testing_number) == number:
            return testing_number
        testing_number += number * step


def generate_min_number(sd):
    count_nine = int(sd / 9)
    search_num = "9" * count_nine
    search_num = int(str(sd % 9) + search_num)
    return search_num


'''
def find_next_number(number,sd):
    	current_sd = sum_digits(number)
    	number = str(number)
		current_position = 0.5 # don't ask me why
		for i in range(1,len(number)):
    			if number[-i] != 9:
    					current_position = -i
						break
		number = 
'''

from sys import argv

while True:
    # N = int(input("Input N: "))
    N = int(argv[1])
    result = find_result_more_effective(N)
    # print("Result: %d" % result)
    # print("\n\n")
    exit()
'''
start = int(input("Input start number: "))
finish = int(input("Input final number: "))
for i in range(start,finish+1):
	result = find_result_more_effective(i)
	i_hope_count_digits = int(i/10)+int(i/9)+1
	print("number: %3d, count digits: %3d, assumption: %3d, k : %-10d , result: %d"%(i,len(str(result)),i_hope_count_digits,int(result/i),result))

'''
