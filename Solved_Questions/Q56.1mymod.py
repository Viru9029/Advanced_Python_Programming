#counts lines first way
def countLines(FileName):
    #open file
    file = open(FileName, mode='r')
    count = 0
    #read file
    read = file.read()
    newline_list = read.split("\n")
    #count line
    for i in newline_list:
        count += 1
    file.close()
    print("Number of lines in the file is", count)
    #return "{} number of lines ".format(count)
#counts lines second way
def countLines2(FileName2):
    file2 = open(FileName2, mode='r')
    counter1 = 0
    for k in file2:
        counter1 += 1
    file2.close()
    print(counter1)

#counts lines third way
def countLines3(FileName3):
    file3 = open(FileName3, mode='r')
    count_line = file3.readlines()
    count1 = len(count_line)
    print(count1)
    file3.close()

#counts lines fourth way
def countLines4(FileName4):
    file4 = open(FileName4, mode='r')
    counter = 0
    file4.readline()
    for i in file4:
        counter += 1
    print("Number of lines in the file is : ", counter)
    file4.close()

#counts character
def countChars(FileName2):
    #open file
    counter = 0
    file2 = open(FileName2, mode='r')
    read_file = file2.read()
    character = read_file.split()
    for j in character:
        counter += 1
    file2.close()
    print("Number of character in the file is : ", counter)

#second way to count character
def countChars1(FileName2):
    file5 = open(FileName2, mode="r")
    a = file5.readline().split()
    count = str()
    for i in range(0,len(a)):
        count = count+a[i]
    print(len(count))


#Test files
def test(FileName3):
    print("Count the lines : ")
    countLines(FileName3)
    print("Count the characters : ")
    countChars(FileName3)

"""print("File Name : " , __name__)
if __name__ == "__main__":
    pass
else:
    print(test("Redable_File.txt"))"""