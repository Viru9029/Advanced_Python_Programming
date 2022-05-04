#Q7: If a five-digit number is input through the keyboard,
# write a program to calculate the sum of its digits without using any loop.
# #(Hint: Use the modulus operator ‘%’)
a = int(input("Enter the five digit number : "))
a5 = a % 10
a4 = (a // 10) % 10
a3 = (a // 100) % 10
a2 = (a // 1000) % 10
a1 = (a // 10000) % 10
a6 = a1+a2+a3+a4+a5
print("Five digit is {} and the sum of digit is {} ".format(a, a6))
