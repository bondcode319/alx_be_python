size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    # (print columns here)
    for col in range(size):
        print("*", end="")
    print()
    row += 1
