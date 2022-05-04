"""
Q4: Write a Python class which has two methods get_String and print_String.
get_String accept a string from the user and print_String print the string in upper case.
"""
class string:
    def get_string(self):
        self.Accept_string = input("Enter the string : ")
        self.upper_case = self.Accept_string.upper()

    def print_string(self):
        print(self.upper_case)

c1 = string()
c1.get_string()
c1.print_string()