#4.  Write a program to print each line of a file in reverse order.
#type 1
file = open("Readable_File.txt","r")
read_file = file.read().split("\n")
l1 = []
for i in read_file:
    l1.append(i)
    l1.reverse()
    file.close()
print(l1)

#type 2
with open("Readable_File.txt","r") as file:
    read_file2 = file.readlines()
    for i in range(0,len(read_file2)):
        l2 = read_file2[i][::-1]
        print(l2)

#type3
with open("Readable_File.txt","r") as file:
    read_file2 = file.readlines()
    for i in range(0,len(read_file2)):
        l2 = read_file2[::-1]
    print(l2)

"""file = open("Readable_File.txt","r")
read_file = file.read().split("\n")
a = read_file.reverse()
file.seek(0)
print(a)
l1 = []
for i in read_file:
    list1 = l1.append(i)
    reverse_order = list.reverse(list1)
    print(reverse_order)"""