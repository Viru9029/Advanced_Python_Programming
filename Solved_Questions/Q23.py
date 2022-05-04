"""Q5: Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string is already ends with 'ing' then add 'ly' instead."""
name_string = str(input("Enter the string : "))
if len(name_string) >= 3:
    if name_string[-3:] == 'ing':
        print(name_string + 'ly')
        #word = name_string+'ly'
        #print(word)
    else:
        print(name_string + 'ing')
        #word1 = name_string+'ing'
        #print(word)
else:
    print("Put string word greater than 3 ")