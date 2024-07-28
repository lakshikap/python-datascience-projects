def pattern_print(n):
    if n % 2 == 0: # n is even
        for i in range(n, 0, -1):
            print("* " * i)
    else: # n is odd
        for i in range(1, n + 1):
            print("* " * i)
        print()
        return pattern_print

number = int(input("Number: "))

print("n=", number)
pattern_print(number)


