#Q3: Write a Python Program to find numbers divisible by thirteen from a list using anonymous function
input_from_user = [int(i) for i in input("Enter the values : ").split()]
find_numbers = list(filter(lambda x : x % 13 == 0, input_from_user))
print("{0} is divisible by thirteen".format(find_numbers))