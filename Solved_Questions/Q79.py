"""
Q5: Write a program to find the area and perimeter of a rectangle using classes
 and objects. Program output should be like this:
"""
#first way
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def Area_of_Rectangle(self):
        self.Area = self.length * self.breadth
        #print(self.length * self.breadth)
        print("Area of rectangle with length {0} and breadth {1} is {2} ".format(self.length, self.breadth, self.Area))

    def Perimeter_of_Rectangle(self):
        self.Perimeter = 2*(self.length + self.breadth)
        #print(2 * (self.length + self.breadth))
        print("Perimeter of rectangle with length {0} and breadth {1} is {2} ".format(self.length, self.breadth,self.Perimeter))


a = int(input("Enter the Length of Rectangle : "))
b = int(input("Enter the Breadth of Rectangle : "))
c1 = Rectangle(a,b)
print("1.Area")
print("2.Perimeter")
print("3.Exit")
while True:
    choice = int(input("Enter your choice : "))
    if choice == 1:
        c1.Area_of_Rectangle()
        print("1.Area")
        print("2.Perimeter")
        print("3.Exit")
    if choice == 2:
        c1.Perimeter_of_Rectangle()
        print("1.Area")
        print("2.Perimeter")
        print("3.Exit")
    if choice == 3:
        print("End of the Program")
        break

#2nd way
"""
class Rectangle:

    def choice1(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print("1.Area")
        print("2.Perimeter")
        print("3.Exit")
        while True:
            choice = int(input("Enter your choice : "))
            if choice == 1:
                self.Area = self.length * self.breadth
                print("Area of rectangle with length {0} and breadth {1} is {2} ".format(self.length, self.breadth,self.Area))
                print("1.Area")
                print("2.Perimeter")
                print("3.Exit")

            elif choice == 2:
                self.Perimeter = 2 * (self.length + self.breadth)
                print("Perimeter of rectangle with length {0} and breadth {1} is {2} ".format(self.length, self.breadth,self.Perimeter))
                print("1.Area")
                print("2.Perimeter")
                print("3.Exit")

            elif choice == 3:
                print("End of the Program")
                break



a= int(input("Enter the Length of Rectangle : "))
b = int(input("Enter the Breadth of Rectangle : "))
c1 = Rectangle()
c1.choice1(a, b)

"""