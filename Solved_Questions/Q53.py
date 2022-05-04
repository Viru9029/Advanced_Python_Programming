#Q5: Write a Python program to find the sum of natural numbers up to n using recursive function
natural_number = int(input("Enter the Natural Number : "))
def sum_of_natural_number(n):
    if n <= 1:
        return n
    else:
        return n + sum_of_natural_number(n - 1)
if natural_number <= 0:
    print("Enter the natural number")
else:
    print("Sum of the Natural number is : ", sum_of_natural_number(natural_number))