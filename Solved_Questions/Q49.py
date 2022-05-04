#Q 1: write a Program to display the Fibonacci sequence up to n-th term where n is provided by the user
# first way
Accept_nth_term = int(input("Enter the Fibonacci Series number of term : "))
nth_1 , nth_2, count = 0 , 1, 0
if Accept_nth_term <= 0:
    print("Enter the positive number")
elif Accept_nth_term == 1:
    print(nth_1)
else:
    while count < Accept_nth_term:
        print("The Fibonacci sequence is : ", nth_1)
        nth_term = nth_1 + nth_2
        nth_1 = nth_2
        nth_2 = nth_term
        count += 1

#second way
def fibonacci_sequence(n):
    n1 = 0
    n2 = 1
    if n <= 0:
        print("Enter the positive number ")
    elif n == 1:
        print(n1)
    else:
        print("Fibonacci Sequnece is :")
        print(n1)
        print(n2)
        for i in range(2, n):
            sum = n1 + n2
            n1 = n2
            n2 = sum
            print(sum)
print(fibonacci_sequence(6))