"""
2. Write a program to implement following.
Create a base class named person consisting of name and code. Create 2 child classes
a)	Account with member_pay
b)	Admin with experience and inherit the base class.

Create a class employee with name, code, experience and pay by inheriting the above classes.

"""
"""class Person:
    Employee_Name = str(input("Enter the Employee Name : "))
    Employee_Code = int(input("Enter the Employee Code : "))

class Account(Person):
    def member_pay(self):
        self.Employee_salary = 20000
        print("Empolyee has Rs.{0} salary.".format(self.Employee_salary))

class Admin(Person):
    Person.Employee_Name
    Person.Employee_Code
    def Experience(self):
        self.Enter_Experience = 5
        print("Employee have {0} years Experience ".format(self.Enter_Experience))

class employee(Account,Admin):
    Admin().Experience()
    Account().member_pay()

c1 = employee()"""

class Person:
    def employee_name_and_code(self):
        self.Employee_Name = str(input("Enter the Employee Name : "))
        self.Employee_Code = int(input("Enter the Employee Code : "))

class Account(Person):
    def member_pay(self):
        self.Employee_salary = 20000
    def display_memebrpay(self):
        print("Empolyee has Rs.{0} salary.".format(self.Employee_salary))

class Admin(Person):
    def Experience(self):
        self.Enter_Experience = 5
    def Accept_All_Input(self):
        self.employee_name_and_code()
        self.Experience()
    def admin_display(self):
        print("Employee Name : ",self.Employee_Name)
        print("Employee Code : ",self.Employee_Code)
        print("Employee have {0} years Experience ".format(self.Enter_Experience))


class employee(Account,Admin):
    def calling_function(self):
        self.Accept_All_Input()
        self.member_pay()
        self.admin_display()
        self.display_memebrpay()

c1 = employee()
c1.calling_function()

