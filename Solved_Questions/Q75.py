"""
Q1: Follow the steps:
•	Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to
    set these appropriately in the body of the __init__()method.
•	Create a variable named number_of_sides and set it equal to 3.
•	Create a method named check_angles. The sum of a triangle's three angles is It should return True if the sum of
    self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
•	Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
•	Print out my_triangle.number_of_sides and print out my_triangle.check_angles().

"""
class Triangle:
    #class variable
    number_of_sides = 3
    #constructor : use to initialize variable
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    #method: check_angle function
    def check_angles(self):
        sum_of_three_angle = self.angle1 + self.angle2 + self.angle3
        print("Sum of triangle is : ",sum_of_three_angle)
        if sum_of_three_angle <= 180:
            return True
        else:
            return False

#Accept anngle sides
Accept_angles1 = int(input("Enter the triangle side angle1 : "))
Accept_angles2 = int(input("Enter the triangle side angle2 : "))
Accept_angles3 = int(input("Enter the triangle side angle3 : "))
#make object and acess Triangle class
my_triangle = Triangle(Accept_angles1,Accept_angles2,Accept_angles3)
#store variable assign value and print
store_value = my_triangle.number_of_sides
print(store_value)
#store boolen value and get control statement correct ouput
store_value1 = my_triangle.check_angles()
print(store_value1)