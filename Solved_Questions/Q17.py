#Q8: a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
string_line = 'restart'
#first way
print('r'+string_line[1:].replace('r', '$'))
print("\n")

#second way
print(string_line[0]+string_line[1:].replace('r', '$'))