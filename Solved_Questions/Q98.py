"""
Q 6: Write a Python program to remove leading zeros from an IP address.
For example:
IP Address 216.08.094.196 dd should be represented as 216.8.94.196
"""
import re
IP_Address = "216.08.094.196"
zero_remove = re.split("0",IP_Address)
word_collector = str()
for i in range(len(zero_remove)):
    word_collector = word_collector + zero_remove[i]
print(word_collector)