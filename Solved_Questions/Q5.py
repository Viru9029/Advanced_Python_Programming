#Q5: Write a Python Program to Solve the quadratic equation ax**2 + bx + c = 0
# Coeffients a, b and c are provided by the user
#[Hint: import complex math module - import cmath]
import cmath
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
d = (b**2) - (4*a*c)
x1 = (-b + cmath.sqrt(d)) / (2*a)
x2 = (-b - cmath.sqrt(d)) / (2*a)
print("Solution of Quadratic equation is : {0} and {1} ".format(x1, x2))
#print("Solution of quadratic equation1 : ", x1)
#print("Solution of quadratic equation2 : ", x2)
