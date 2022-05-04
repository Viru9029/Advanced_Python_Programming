"""Q11: Given a Python list. Write a python program to turn every item of a list into its
square
List1 = [1, 2, 3, 4, 5, 6, 7]
Expected output:
[1, 4, 9, 16, 25, 36, 49]"""
l = list()
list1 = [1, 2, 3, 4, 5, 6, 7]
for i in list1:
    l.append(i ** 2)
print(l, end=" ")
