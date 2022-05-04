#2. Write a Python program to append text to a file and display the text.
#n = int(input("Enter the Number to read lines upto : "))

text = input("Enter the Text : ")
File = open("Readable_File2.txt", "a+")
File.write(text)
File.seek(0)
print(File.read())


File = open("Readable_File2.txt", "a+")
n = int(input("Enter the number of lines : "))
for i in range(1, n):
    print("Enter the Text{%d}" %i)
    text = input()+" "
    #text1 = text+" "
    File.write(text)
    #File.write(text1)
File.seek(0)
print(File.read())
File.close()



