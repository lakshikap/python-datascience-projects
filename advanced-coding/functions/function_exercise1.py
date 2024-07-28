def check_number(number):
    if number % 2 == 0:
        return False

    if number < 2:
        return False

    for i in range(2, number//2):
        if number % i == 0:
            return False

    return True

number_x = input("Type a number: ")
number_x = int(number_x)

print(check_number(number_x))
