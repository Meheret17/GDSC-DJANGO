string = input('enter a character to be printed ')
for i in range(5):
    pattern = string * (2*i+1)
    print(pattern)