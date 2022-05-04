#Q 3: Write a Python  Program to handle multiple errors with one except statement
import sys
try:
    a = 10
    b = 0
    print(a/b)
    l1 = [10,20,30,40]
    print(l1[6])
    str1 = Hello
    print(str1)

except (ZeroDivisionError,IndexError,NameError):
    print("Error : ", sys.exc_info()[0])
    print("Error Description : ", sys.exc_info()[1])
    print("Error object : ", sys.exc_info()[2])
    print("Error : {0} ,Error Description : {1} , Error object : {2} ".format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]))

finally:
    print("""Note : 1.If it showing any error in program please solve it\
    2.If it showing deserved output Program run sucessfully """)
"""
except:
    print("Please enter positive value for division")
    print("Index is out of range Please enter right index number ")
    print("Please enter name in string format use single quote,double quote and triple quote ")
"""