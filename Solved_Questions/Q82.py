"""
3. Write program to create a base class staff with code and name. Derive classes teacher(subject , publication) , typist (speed) , officer (grade) .
Using the typist class as base class,create two classes regular(salary) and  casual(daily wages).Implement a menu driven program for the same.

Output:
1.	Teacher
2.	Officer,
3.	Regular Typist
4.	Casaul typist
5.	Exit

"""
class Staff:
    def employee_name_and_code(self):
        self.Employee_Name = str(input("Enter the Employee Name : "))
        self.Employee_Code = int(input("Enter the Employee Code : "))

class Teacher(Staff):
    def subject(self):
        print("Subject : English")
    def publication(self):
        print("Punlication : Balbharti")
    def T_display(self):
        self.employee_name_and_code()
        print(self.Employee_Name)
        print(self.Employee_Code)
        self.subject()
        self.publication()


class typist(Staff):
    def speed(self):
        print("Speed : 90 WPM(Words Per Minutes)")

class officer(Staff):
    def grade(self):
        print("Officer Grade : A+ ")
    def office_display(self):
        self.employee_name_and_code()
        print(self.Employee_Name)
        print(self.Employee_Code)
        self.grade()

class regular(typist):
    def salary(self):
        print("Regular Typist has Rs.16500 Salary Per Month.")
    def Typist_display(self):
        self.employee_name_and_code()
        print(self.Employee_Name)
        print(self.Employee_Code)
        self.speed()
        self.salary()

class casual(typist):
    def daily_wages(self):
        print("Casual Typist has Rs.265 Salary Per Hour. ")
    def casual_display(self):
        self.employee_name_and_code()
        print(self.Employee_Name)
        print(self.Employee_Code)
        self.speed()
        self.daily_wages()

while True:
    print("*** List of Staff ***")
    print("1.Teacher")
    print("2.Officer")
    print("3.Regular Typist")
    print("4.Casaul typist")
    print("5.Exit")
    choice = int(input("Enter the number : "))
    if choice == 1:
        c1 = Teacher()
        c1.T_display()
    if choice == 2:
        c1 = officer()
        c1.office_display()
    if choice == 3:
        c1 = regular()
        c1.Typist_display()
    if choice == 4:
        c1 = casual()
        c1.casual_display()
    if choice == 5:
        print("DATA SAVE SUCCESSFULLY")
        break
