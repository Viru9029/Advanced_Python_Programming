#Q9: Write a python program to raise an error and stop the program if x is lower than 0.
import sys
class Error(Exception):
    """Base class of User defined error"""

class NegativeValueNotAllowed(Error):
    """class of lower than 0 values"""

class PositiveValueAllowed(Error):
    """class of positive value greater than 0"""
Flag = False
while True:
    try:
        num1 = int(input("Enter the Negative value : "))
        if num1 <= 0 :
            raise NegativeValueNotAllowed


        if num1 > 0 :
            raise PositiveValueAllowed

    except NegativeValueNotAllowed:
        print("Please enter the positive value")
        break

    except PositiveValueAllowed:
        print("All right! No need to change")
    #except:
        #print("Error : {0} \nError Description : {1} \nError object : {2}  ".format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]))
