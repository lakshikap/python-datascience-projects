# n = input("Enter a number: ")
# n = int(n)

# if n % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

indian = ["samosa", "dhal", "naan"]
chinese = ["egg roll", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name: ")
if dish in indian:
    print(f"{dish} is indian")
elif dish in chinese:
    print(f"{dish} is chinese")
elif dish in italian:
    print(f"{dish} is italian")
else:
    print("I don't know which cuisine is this!")