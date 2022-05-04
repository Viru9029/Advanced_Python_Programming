#Q1: Write a python program to add all the odd numbers from 0 to 20.
"""sum = 0
for i in range(21):
    if i % 2 != 0:
        print("0 - 20 odd no is : ", i)
        sum = sum+i
print("Sum of odd no is : ", sum)"""
square = [i % 2 != 0 for i in range(21)]
print(square)