#1.  Write a Python program to read first n lines of a file.
n = int(input("Enter the Number to read lines upto : "))
file = open("Readable_File.txt", "r")
read_file = file.read().split("\n")
count = 0
#file.seek(0)
for i in read_file:
    count += 1
    print(i)
    if count == n:
        break
    else:
        pass
    file.close()