number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = float(input('Enter Third number : '))
def largest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
    print("The largest of the 3 numbers is : ", largest_num)

largest(number1, number2, number3)

