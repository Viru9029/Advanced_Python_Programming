#Q2: Write a Python Program to Display Powers of 2 Using Anonymous Function
#( Lambda function). Take number of terms from user
list1 = [1, 2, 3, 4, 5, 6, 7]
square = list(map(lambda x : 2 ** x , list1))
print(square)

#second way
input_from_user = [int(x) for x in input("Enter the numbers : ").split()]
power_value = list(map(lambda y : 2 ** y, input_from_user))
print(power_value)