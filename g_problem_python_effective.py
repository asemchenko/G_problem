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
def find_element_in_array(element,array):
	for i in range(0,len(array)):
		if array[i] == element:
			return i
	return -1
def find_next_number(number_array,need_sum_digits):
	current_sd = -1
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
def fast_division_check(reversed_digits,koef,index_repeat,number_division):
	k = 0
	result = 0
	index = 0
	while k < len(reversed_digits):
		result+= (koef[index]*reversed_digits[k])%number_division
		result = result%number_division
		k+=1
		if index < len(koef) -1 :
			index +=1
		else:
			index = index_repeat
	return result%number_division
def find_koef(number):
    koef = [1]
    current_koef = 0
    while True:
    	current_koef = (koef[len(koef)-1]*10)%number
    	if not(current_koef in koef):
    		koef.append(current_koef)
    	else:
    		break
    index_repeat = find_element_in_array(current_koef,koef)
    return koef,index_repeat
def find_result(number):
	coef_for_number,index_repeat = find_koef(number)
	start_number = generate_min_number(number)
	digits_int_start_number = reverse(start_number)
	while True:
		if fast_division_check(digits_int_start_number,coef_for_number,index_repeat,number) == 0:
			return get_number_from_reversed_array(digits_int_start_number)
		find_next_number(digits_int_start_number,number)
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
		start+=1

