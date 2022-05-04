#Q7: Print one message if the try block raises a NameError and another for other errors:
import sys
try:
    a = 5
    b = "char"
    value = 10
    print("Value : ", valu)
    print(a/b)

except (NameError,TypeError):
    print("Error : {0} \nError Description : {1} \nError Object : {2} ".format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]))

""" 
except NameError:
        print("Please check variable name ")

except TypeError :
        print("Please enter positive value in division not string value")

"""