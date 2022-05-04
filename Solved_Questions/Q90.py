#Q8: Try to open and write to a file that is not writable:
import io
import sys
try:
    file = open("Redable_File.txt", "r")
    file.write("Hello Cdac Noida")
    file.seek(0)
    print(file.read())

except io.UnsupportedOperation:
    print("Error : {0} \nError Description : {1} \nError object : {2} " .format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2]))
    print("Please check the mode of file")

finally:
    print("File successfuly closed!")
    file.close()

