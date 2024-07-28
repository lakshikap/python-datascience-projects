# Define the number of rows

#for i in range(5, 0, -1):
#    print(i)


num_rows = 5
# Outer loop for each row
for i in range(num_rows, 0, -1):

    # Inner loop for printing numbers in each row
    for j in range(1, i + 1):
        print(j, end=' ')
    # Print a newline after each row
    print()
