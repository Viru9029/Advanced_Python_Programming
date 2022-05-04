#Q5: Write a Python Program to depict Raising Exception
import sys
try:
    num = int(input("Enter Even No : "))
    if num % 2 == 0:
        print("Even No : ", num)
    else:
        raise ValueError("This is not EVEN no Please Enter EVEN No")

except ValueError as e :
    print("Error is : " , e)

#second way
#except:
    #print(sys.exc_info()[0])