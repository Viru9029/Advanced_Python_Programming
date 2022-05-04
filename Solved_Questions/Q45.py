"""Q15: Write a python program to print the Following:
1
2 1
3 2 1"""
for i in range(1, 2):
    print(i)
    for j in range(2, 0, -1):
        print(j, " ", end=" ")
    print()
    for k in range(3, 0, -1):
        print(k, " ", end=" ")