#Q1: Write a function to compute 5/0 and use try/except to catch the exceptions.
import sys
a = 5
b = 0
try:
    division = a/b

except ZeroDivisionError as v:
    print("Error : ",v)

finally:
    print("""Note : 1.If it showing any error in program please solve it\
    2.If it showing deserved outpute Program run sucessfully """)

"""
except:
    print("Error : ",sys.exc_info()[0])
    print("Error Description : ", sys.exc_info()[1])
    print("Error Object : ", sys.exc_info()[0])
    
except:
    print("Please do not enter 0 in denominator of division")
    
except ZeroDivisionError:
    print("Please do not enter 0 in denominator of division")
"""