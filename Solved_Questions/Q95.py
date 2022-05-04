#Q3 : Write a Python program to search some literals strings in a string.
import re
string = "Hello, my name is Virendra Kate."
output = re.search('Virendra',string,flags=re.IGNORECASE)
if output != None:
    print("Match at index : %s %s " %(output.start(),output.end()))
    print("Full Match : %s" %(output.group()))
else:
    print("The pattern does not match.")