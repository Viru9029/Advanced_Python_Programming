#1. Write a Python program to read an entire text file.

#first way
read_file = open(r"Redable_File.txt", mode="r")
print(read_file.read())
read_file.close()

"""
#second way
read_file = open("V:\\PG-DAI\\1.Python\\Day 10\\Lab Exercise 6\\Lab_Exercise_5.py", mode="r")
#third way
read_file = open("V:/PG-DAI/1.Python/Day 10/Lab Exercise 6/Lab_Exercise_5.py", mode="r")
#fourth way"""
#read_file = open("""V:\PG-DAI\1.Python\Day 12\Exercise No 6\Lab_Exercise_5.py""", mode="r")