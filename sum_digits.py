def sum_digits(number):
	number_str = str(number)
	summa = 0
	for digit in number_str:
		summa += int(digit)
	return summa

while True:
	num = int(input("Input number: "))
	print("Result : %d"%sum_digits(num))
	print("\n")

