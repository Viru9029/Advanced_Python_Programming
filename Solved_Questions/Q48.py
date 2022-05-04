"""
Q18: Write a python program to print following multiplication table on the screen

"""
for i in range(0, 11):
    print("\t",i, end="\t")
print()
print("    +", end="")

for i in range(1, 14):
    print(i * '-', end="")
print()
for j in range(1, 11):
    if j < 10:
        print("", end="")
    print(j, "  | ", end="\t")
    for k in range(1, 11):
        print("\t", j * k, end="\t")
    print()



"""
fifth way

for i in range(1, 11):
    print("\t", "{0:4d}".format(i), end=" ")
print()
print("", end="")
print("     +---------------------------------------------------------------------------------")
for i in range(1, 11):
    print("{0:4d} |".format(i), end="\t")
    j = 1
    k = 10
    while(j<=10):
        print("{0:4d}".format(j * i), end="\t")
        j += 1
    print()



fourth way
for k in range(1, 11):
    print("\t","\t",k, end="\t")
print()
print("\t","+","-" * 120 , end="\t")
print()
for x in range(1, 11):
    for j in range(1, 11):
        print(x * j,"\t","|", end="")
    print()
    
    
third way
for k in range(1, 11):
    print(k, end="   ")
print()
for l in range(10):
    print(l * "-", end="")
        for i in range(1, 11):
            for j in range(1, 11):
                print(i * j, end="\t")
        print()
print()
for k in range(1, 11):
    print(k,)
print()


#First way
for i in range(1, 11):
    print(i, " ", i * 2, "  ", i * 3, "  ", i * 4, "  ", i * 5, "  ", i * 6, "  ", i * 7, "  ", i * 8, "  ", i * 9, "  ", i * 10 )
    
#second way
for i in range(1, 11):
    print(i, "    ", end=" ")
print()
for j in range(1, 11):
    print(j * 2, "    ", end=" ")
print()
for k in range(1, 11):
    print(k * 3, "    ", end=" ")
print()
for l in range(1, 11):
    print(l * 4, "    ", end=" ")
print()
for m in range(1, 11):
    print(m * 5, "    ", end=" ")
print()
for n in range(1, 11):
    print(n * 6, "    ", end=" ")
print()
for o in range(1, 11):
    print(o * 7, "    ", end=" ")
print()
for p in range(1, 11):
    print(p * 8, "    ", end=" ")
print()
for q in range(1, 11):
    print(q * 9, "    ", end=" ")
print()
for r in range(1, 11):
    print(r * 10, "    ", end=" ")
"""
"""1   2    3    4    5    6    7    8    9    10
2   4    6    8    10    12    14    16    18    20
3   6    9    12    15    18    21    24    27    30
4   8    12    16    20    24    28    32    36    40
5   10    15    20    25    30    35    40    45    50
6   12    18    24    30    36    42    48    54    60
7   14    21    28    35    42    49    56    63    70
8   16    24    32    40    48    56    64    72    80
9   18    27    36    45    54    63    72    81    90
10   20    30    40    50    60    70    80    90    100"""