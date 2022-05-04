#Q1: Write a Python program which accept the radius of a circle from the user
#and compute the area.
#Sample Output : 
#r = 1.1
#Area = 3.8013271108436504

import math
radius = float(input("Enter the radius of circle : "))
area = math.pi * pow(radius,2)
#area = 3.14 * (radius**2)
print("Area of circle is : ",area)
