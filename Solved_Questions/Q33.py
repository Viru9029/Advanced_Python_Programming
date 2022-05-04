#Q3: Write a program to display the sum of square of the first ten even natural numbers
#// (2*2+ 4*4 + 6*6 + 8*8 + 10*10 + 12*12 + 14 * 14 + 16 * 16 + 18*18 + 20*20)
sum = 0
for i in range(2, 21, 2):
    square = i ** 2
    print(square)
    if square % 2 == 0:
        sum = sum +square
    else:
        pass
print("Sum of the square of the first ten even natural number is : ", sum)