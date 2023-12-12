sum = 0
for item in range(1,51):
    if item%2 == 0:
        if item%3 == 0:
            print("Three")
        elif item%5 == 0:
            print("Five")
        else:
            print(item)
sum+=item
print("sum=" , sum)
