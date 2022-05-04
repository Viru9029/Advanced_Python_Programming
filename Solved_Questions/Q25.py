#Q7: write a Python program to find the largest number among the three input numbers
number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number : "))
number3 = int(input("Enter the third number : "))
if number1 > number2 and number1 > number3:
    print("Largest number is : ", number1)
elif number2 > number1 and number2 > number3:
    print("Largest number is : ", number2)
else:
    print("Largest number is : ", number3)