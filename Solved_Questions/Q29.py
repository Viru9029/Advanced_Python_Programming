"""Q11: Given a nested list. Write a python program to extend it with adding sub list ["h", "i", "j"]
in a such a way that it will look like the following list
Given List:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sub List to be added = ["h", "i", "j"]
Expected output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']"""
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l]", "m", "n"]]
sub_list = ["h", "i", "j"]
modified_list = list1[2][1][2].extend(sub_list)
print("Modified list : ", list1)