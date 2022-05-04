"""Q12: Write a python program for Given a Python list, to find value 20 in the list, and if it is
present, replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output:
list1 = [5, 10, 15, 200, 25, 50, 20]"""
list1 = [5, 10, 15, 20, 25, 50, 20]
find_value = list1.index(20, 0, 6)
print("20 Value index is : ", find_value)
list1[find_value] = 200
print("Modified list is : ", list1)

#second way
if find_value != -0:
    list1[find_value] = 200
    print("Modified list is : ", list1)
else:
    pass