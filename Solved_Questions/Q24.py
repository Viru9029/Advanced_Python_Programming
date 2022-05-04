"""Q6: The marks obtained by a student in 5 different Subjects are input through a keyboard. The
Student gets a division as per the following rules.
1. Percentage above or equal to 60 – First Division
2. Percentage between 50 and 59 – Second Division
3. Percentage between 40 and 49 – Third Division
4. Percentage less than 40 – Fail
Write a python program to Display the result based on the above Criteria."""
#first method
subject1 = int(input("Enter the marks of English subject : "))
subject2 = int(input("Enter the marks of Hindi subject : "))
subject3 = int(input("Enter the marks of Marathi subject : "))
subject4 = int(input("Enter the marks of History subject : "))
subject5 = int(input("Enter the marks of Mathematics subject : "))
sum_of_all_subjects = subject1+subject2+subject3+subject4+subject5
percentage = ((sum_of_all_subjects / 500) * 100)
if percentage >= 60:
    print("You got {%.2d} and First Class"% percentage)
elif percentage >= 50:
    print("You got {%.2d} and Second Division"% percentage)
elif percentage >= 40 :
    print("You got {%.2d} and Third Division"% percentage)
else :
    print("You got {%.2d} and You are Fail"% percentage)

#second method
