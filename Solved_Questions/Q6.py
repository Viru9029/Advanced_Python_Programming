#Q6: Write a Python Program to find the area of triangle
# Three sides of the triangle a, b and c are provided by the user
import math
a = int(input("Enter the first side of triangle : "))
b = int(input("Enter the second side of triangle : "))
c = int(input("Enter the third side of triangle : "))
#semiperimeter = s
s = (a+b+c)/2
areaoftriangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of Triangle is : ", areaoftriangle)

#Area of triangle
base = 4
height = 5
area = (1/2)*(base * height)
print("Area of Triangle :  ", area)


