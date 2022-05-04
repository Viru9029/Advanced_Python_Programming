#Q5: Replace all occurrences of note irrespective of case with X in given string i.e. 'This note should not be NoTeD'.
import re

given_string = "This note should not be NoTeD"
find_and_replace = re.sub(" note "," X ",given_string,flags=re.IGNORECASE)
print(find_and_replace)