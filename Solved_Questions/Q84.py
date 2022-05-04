#Q2: Write a Python program to access the array element whose index is out of bound and handle
# the corresponding exception
import sys
try:
    l1 = [1, 2, 3, 4, 5, 6, 7]
    value = l1[9]
    print(value)

except IndexError as error:
    print("Error is : ", error)

finally:
    print("""Note : 1.If it showing any error in program please solve it\
    2.If it showing deserved outpute Program run sucessfully """)

"""
except:
    print("Error : ", sys.exc_info()[0])
    print("Error Description : ", sys.exc_info()[1])
    print("Error object : ", sys.exc_info()[2])
    
except IndexError:
    print("Array list is out of range please enter correct index number.")
    
except:
    print("Array list is out of range please enter correct index number.")
"""