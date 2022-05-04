#6. Write a program to compute the number of characters, words and lines in a file.
with open("Readable_File.txt","r") as file:
    read_file = file.read().split()
    print("Total number of words present in file is : ", len(read_file))
    character_store = str()
    for i in read_file:
        character_store += i
    print("Total numbers of character present in file is : ", len(character_store))
    file.seek(0)
    count_lines = file.readlines()
    print("Total numbers of lines present in file is : ",len(count_lines))



