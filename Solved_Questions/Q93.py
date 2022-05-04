#Q1: Write a Python program that matches a string that has an a followed by zero or more b's.
import re
ans1 = re.findall("ab*" , "ababbbbabbababababbbbaabaabaaab")
print(ans1)

"""

#2nd way
ans1 = re.findall("ab*" , "ababbbbabbababababbbbaabaabaaab" , flags=re.IGNORECASE)
print(ans1)

#1st way
string1 = re.compile('ab*')
ans = string1.findall("ababbbbabbababababbbbaabaabaaab")
print(ans)
"""