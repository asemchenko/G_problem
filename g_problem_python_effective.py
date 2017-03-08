def reverse(number):
	number_str = str(number)
	number_array_reverse = []
	i = len(number_str)-1
	while i > -1:
		number_array_reverse.append(int(number_str[i]))
		i-=1
	return number_array_reverse
def find_less_element(array,element):
	i = 1
	while i < len(array):
		if array[i] < element:
			return i
		i+=1
	return -1
def sum_digits(number_array):
	summa = 0
	for element in number_array:
		summa += element
	return summa
def write_number(start_index,final_index,array,number):
	k = start_index
	while k < final_index:
		array[k] = number
		k+=1
def find_next_number(number_array):
	need_sum_digits = sum_digits(number_array)
	current_sd = -1
	if need_sum_digits & 1 == 0:
		while current_sd != need_sum_digits:
			element_less_than_nine_ind = find_less_element(number_array,9)
			if element_less_than_nine_ind < 0:
				number_array.append(0)
			element_less_than_nine_ind = find_less_element(number_array,9)
			write_number(0,find_less_element(number_array,9),number_array,0)
			number_array[element_less_than_nine_ind] += 1
			current_sd = sum_digits(number_array)
			if current_sd == need_sum_digits:
				break
			delta = need_sum_digits - current_sd
			if delta < 0 :
				continue
			if delta > 8:
				number_array[0] = 8
				delta -= 8
				count_nine = int(delta/9)
				write_number(1,count_nine+1,number_array,9)
				delta -= count_nine*9
				if count_nine+1 != len(number_array)-1:
					number_array[count_nine+1] = (delta)%9
			else:
				count_nine = int(delta/9)
				write_number(0,count_nine,number_array,9)
				number_array[count_nine] = delta%9
			current_sd = sum_digits(number_array)
	else:
		while current_sd != need_sum_digits:
			element_less_than_nine_ind = find_less_element(number_array,9)
			if element_less_than_nine_ind < 0:
				number_array.append(0)
			element_less_than_nine_ind = find_less_element(number_array,9)
			write_number(0,find_less_element(number_array,9),number_array,0)
			number_array[element_less_than_nine_ind] += 1
			current_sd = sum_digits(number_array)
			if current_sd == need_sum_digits:
				break
			delta = need_sum_digits - current_sd
			if delta < 0 :
				continue
			count_nine = int(delta/9)
			#if (count_nine) and is_number_even == 1:
				#continue
			write_number(0,count_nine,number_array,9)
			number_array[count_nine] = delta%9
			current_sd = sum_digits(number_array)
def generate_min_number(sd):
	count_nine = int(sd/9)
	result = "9" * count_nine
	result = str(sd%9) + result
	return int(result)
def get_number_from_reversed_array(array):
	number_string = ""
	array.reverse()
	for element in array:
		number_string += str(element)
	array.reverse()
	return int(number_string)
def fast_division_check(number,division_number):
	for i in range(1,7):
		if division_number % i == 0:
			if  number % i != 0:
				return 0
	return 1
def find_koef(number):
    koef = [1]
    for i in range(1,number+1):
        current_coef = (koef[i-1]*10)%number
        if current_coef != 1:
            koef.append(current_coef)
        else:
            break
    return koef
def get_info_about_modulo(digits_array,coeficients,number):
    result = 0
    for i in range(0,len(digits_array)):
        result += (digits_array[i]*coeficients[i%len(coeficients)])%number
    result = result%number
    return result
def find_result(number):
	coef_for_number = find_koef(number)
	start_number = generate_min_number(number)
	digits_int_start_number = reverse(start_number)
	while True:
		if get_info_about_modulo(digits_int_start_number,coef_for_number,number) == 0:
			return get_number_from_reversed_array(digits_int_start_number)
		find_next_number(digits_int_start_number)
		#print(start_number)
'''
while True:
	number = int(input("Input number: "))
	count_needed_numbers = int(input("Input count_needed numbers: "))
	digits_array = reverse(number)
	print("Sd: %d"%sum_digits(digits_array))
	for dz in range(0,count_needed_numbers):
		find_next_number(digits_array)
		print("Result: ",end = "")
		digits_array.reverse()
		for element in digits_array:
			print(element,end="")
		print(" %d"%get_number_from_reversed_array(digits_array))
		print()
		digits_array.reverse()
'''

while True:
	N = int(input("Input N: "))
	res = find_result(N)
	print("Result: %d"%res)
	print("\n")
'''
while True:
	start = int(input("Input start number: "))
	stop = int(input("Input stop number: "))
	while start <= stop :
		print("number: %3d , result: %d"%(start,find_result(start)))
		start+=2
'''
