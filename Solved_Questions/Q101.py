people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}
print("Total no of student present in list is : ",len(people))#Q1.Find out how many students are in list.
#Q.2 Change lisa's favourite colour
Colour = input("Enter the lisa's favourite color here : ")
people['Lisa'] = Colour
print("After changing lisa's colour output is : ",people)
#Q.3 Remove 'Jenny' and her favourite colour
del people['Jenny']
print("After removing 'Jenny' and her favouitr colour output is : ",people)
#Q.4 Sort and print students and their favourite colours alphabetically by name
store_in_list = []
store_in_list.extend(people)
store_in_list.sort()
for key in store_in_list:
    print(key, ':', people[key]," , ",end=" ")