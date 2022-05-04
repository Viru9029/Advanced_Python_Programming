#Q9: Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
str1 = 'abc'
str2 = 'xyz'
#first way
replace = str2.replace('z', 'c')+ " " +str1.replace('c', 'z')
print(replace)
print("\n")

#second way
replace2 = (str2[0:2]+str1[2:])+ " " +(str1[0:2]+str2[2:])
print(replace2)