#3. Test your mymod module from Exercise 2 interactively, by using from to load the exports directly,
# #first by name, then using the from* variant to fetch everything.
print("*** 1 ***")
import mymod as a
a.countLines("Redable_File.txt")
a.countChars("Redable_File.txt")
a.test("Redable_File.txt")

print("*** 2 ***")
from mymod import countLines , test
countLines("Redable_File.txt")
test("Redable_File.txt")

print("*** 3 ***")
from mymod import countLines , countChars
countLines("Redable_File.txt")
countChars("Redable_File.txt")

print("*** 4 ***")
from mymod import *
countLines("Redable_File.txt")
countChars("Redable_File.txt")
test("Redable_File.txt")

print("*** 5 ***")
from mymod import countLines as b
b("Redable_File.txt")