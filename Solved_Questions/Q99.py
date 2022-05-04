def palindrome():
    palindrome_pharse = input("Enter the palindrome phrase here : ")
    store_character=""
    for i in range(len(palindrome_pharse)):
        #first remove the symbol on given string adding character one by one when character is alphabet then it will added.
        if palindrome_pharse[i].isalpha():
            store_character+=palindrome_pharse[i]
    print(store_character)#after removing punctuation, capitalization, and spacing output is store here.
    if store_character.lower() == store_character[::-1].lower():#check the condition of palindrome
        print("Right! Given string is Palindrome")
    else:
        print("Sorry! Given string is not palindrome")

palindrome()