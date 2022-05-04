#Q10: write a Program to sort alphabetically the words form a string provided by the user.
# You can use split() method to split string into a list of words.
string1 = input("Enter the string : ")
split_string = string1.split()
sorting_string = sorted(split_string)
print("Before sorting string is : {0} and After sorting string is : {1} ".format(split_string, sorting_string))