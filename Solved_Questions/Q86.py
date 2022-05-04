#Q 4: Write a Python Program to depict else clause with try-except
import sys
value = int(input("Enter the value : "))

try:
    if value <= 10:
        print("Value : ",value)
    else:
        print("Value : ",valu)
except:
        print("Error : {0} \nError Description : {1} \nError object : {2}  ".format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]))
        print("Error : You enter wrong variable name Please enter right name")
else:
    print("Your Output Is Correct!")

finally:
    print("Program Run Successfuly!")

