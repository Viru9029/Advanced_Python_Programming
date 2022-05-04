#Q4: Replace all occurrences of 5 with five for the given string i.e. 'They ate 5 apples and 5 oranges'
import re

given_string = "They ate 5 apples and 5 oranges"
find_and_replace = re.sub(" 5 "," Five ",given_string)
print(find_and_replace)