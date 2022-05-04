#Q6: Write a Python program to convert decimal number into binary number using recursive function
import math
"""def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end="")"""
def decimal_to_binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * (decimal_to_binary(n // 2))

Accept_No = int(input("Enter the decimal number : "))
print(decimal_to_binary(Accept_No))
