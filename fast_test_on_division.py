def find_koef(number):
    koef = [1]
    for i in range(1,number+1):
        current_coef = (koef[i-1]*10)%number
        if current_coef != 1:
            koef.append(current_coef)
        else:
            break
    return koef

while True:
    num = int(input("Input number: "))
    res = find_koef(num)
    print("Result: ")
    for element in res:
        print("%d"%element)
    print("len: %d"%len(res))
    print("\n")