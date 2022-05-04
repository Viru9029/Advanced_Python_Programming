#Q10: Write a python program to raise a TypeError if x is not an integer:
import sys
try:
    x = input("Enter the str : ")
    sum = x + 12
    print(sum)

except TypeError:
    print("Error : {0} \nError Description : {1} \nError object : {2} ".format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]))
    print("Please Enter integer input")
