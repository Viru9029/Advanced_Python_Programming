#Q2: Write a Python program to check for a number at the end of a string.
import re
string1 = "Hello My Name is Virendra Kate . My roll no is 23562"
regex = "$23562"
check_number_at_end = re.findall("\d+$" , string1)
if check_number_at_end:
    print("Yes string end with number.")
else:
    print("No match")
print(check_number_at_end)
