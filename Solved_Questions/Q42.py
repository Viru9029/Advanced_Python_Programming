#Q12: Program to count the number of each vowel in a string.
string_name = "india is my country"
l1 = ["a", "e", "i", "o", "u"]
count = {}.fromkeys(l1, 0)
for char in string_name:
    if char in count:
        count[char] += 1
print("Vowels count in the string is : ", count)