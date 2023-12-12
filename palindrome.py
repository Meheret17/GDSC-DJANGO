string = input("please enter the word to check: ")
if string == string[::-1]:
    print(string , " is palindrome")
else:
    print(string , " is not palindrome")