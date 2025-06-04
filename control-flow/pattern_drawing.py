length = int(input("Enter the size of the pattern:"))
i = 0

if length < 0:
    print("Error! Please input a positive integer")
else:
    while i < length:
        j = 0
        for j in  range(length):
            print("*", end="")
        print()
        i += 1
