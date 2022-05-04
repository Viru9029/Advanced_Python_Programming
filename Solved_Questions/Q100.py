chipherDic = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't',
              'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
              'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
              'A': 'N', 'B': 'O', 'C': 'P',
              'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T',
              'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D',
              'R': 'E', 'S': 'F',
              'T': 'G', 'U': 'H', 'V': 'I',
              'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

chipherText = input("Enter the chiper text")
# Empty String for Keeping Our decoded chipher text
decode = ""

for i in range(len(chipherText)):
    # This will filter out special symbols and numerics
    if chipherText[i].isalpha():
        decode += chipherDic[chipherText[i]]
    else:
        decode += chipherText[i]
    # end of if
# End of for loop

print("Decoded text is", decode)


