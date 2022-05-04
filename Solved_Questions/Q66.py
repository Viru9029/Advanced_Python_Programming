#5. Write a Python program to write a list content to a file.
with open("Readable_File2.txt","w+") as file:
    l1 = [900,20,30,40,50,60,70,80,90,100]
    file.writelines(str(l1))
    file.seek(0)
    print(file.read())

#second way
with open("Readable_File2.txt", "a+") as file:
    l1 = ["Hello", "World"]
    file.writelines(l1)
    file.seek(0)
    print(file.read())