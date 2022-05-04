#Q4: Write a Python program to display the Fibonacci sequence up to n-th term by using recursive functions
def fibonacci_seq(num):
    if num <= 1:
        return num
    else:
        return (fibonacci_seq(num-1) + fibonacci_seq(num - 2))

input_nth_term = int(input("Enter the nth term : "))
if input_nth_term <= 0:
    print("Enter the positive no")
else:
    print("Fibonacci Sequence : ")
    for i in range(input_nth_term):
        print(fibonacci_seq(i))