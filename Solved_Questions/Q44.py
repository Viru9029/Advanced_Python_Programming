"""Q 14: write a Program to Remove Punctuations from a String provided by the user. [Hint: use
punctuation attribute of string module to get all punctuations (i.e. !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ )
"""
#my_str = str(input("Enter the string with Punctuations: "))
my_str = "Hello!!!World!!!!, ---$#%%%%^Hello@#$%@#%World."
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punctuations = ""
for char in my_str:
    if char not in punctuations:
        no_punctuations = no_punctuations + char
print(no_punctuations)