try:
    lst = [int(x) for x in input().split()]
    i = int(input("Enter Index: "))
    print(lst[i])
except ValueError:
    print("Error: Please enter valid integers.")
except IndexError:
    print("Error: Index is out of range.")
