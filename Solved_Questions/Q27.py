#Q9: write a Program to check if a string is palindrome or not eg 1.madam 2.nursesrun
string_name = str(input("Enter the string : "))
length_of_string = int(len(string_name))
if string_name == string_name[length_of_string::-1]:
    print("{0} String is Palindrome.".format(string_name))
else:
    print("{0} string is not Palindrome.".format(string_name))