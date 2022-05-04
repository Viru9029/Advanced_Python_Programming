"""
Q17: WAP to create a function traiangle to print the following asterisk triangle pattern:
*
* *
* * *
* * * *
* * *
* *
*
"""
for i in range(1, 5):
    print(i * " * ")
for j in range(3, 0, -1):
    print(j * " * ")