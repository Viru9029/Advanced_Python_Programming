"""2. Write a program that counts lines and characters in a file. With your favorite text editor, code a Python module
called mymod_1.py, which exports three top-level names:
a) A countLines(name) function that reads an input file and counts the number of lines in it
b) A countChars(name) function that reads an input file and counts the number of characters in it
c) A test(name) function that calls both counting functions with a given input filename.
All three mymod functions should expect a filename string to be passed in. Now, test your module interactively,
using import and name qualification to fetch your exports."""

import mymod
print(mymod.countLines("Redable_File.txt"))

print(mymod.countChars("Redable_File.txt"))

print(mymod.test("Redable_File.txt"))

