#3. Write a Python program to read a file line by line and store it into a list.
file = open("Readable_File.txt", "r")
read_lines = file.read().split("\n")
#print(read_lines)
l1 = []
count = 0
for i in read_lines:
    count += 1
    l1.append(i)
print(l1)
print("No of lines : ", count)
file.close()

#second way
file1 = open("Readable_File.txt", "r")
read_lines1 = file1.readlines()
print(read_lines1)
file1.close()