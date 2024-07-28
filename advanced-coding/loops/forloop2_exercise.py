#totals = 0
#for i in range(1, 21, 2):
#    totals = i + totals
#print(totals)

#sum_even = 0
#number = 0

#while number <= 20:
#    if number % 2 == 0:
#        sum_even = sum_even + number
#    number = number + 1
#print("The sum of all even numbers: ", sum_even)

#dice_result = [5, 6, 4, 2, 5, 4, 4, 5, 3, 3, 2, 6, 1, 2, 1, 1, 6, 5]
#count_sixes = 0

#for result in dice_result:
#        if result == 6:
#                count_sixes = count_sixes + 1
#print("The number six was rolled:", count_sixes, " times.")


#dice_result = [5, 6, 4, 2, 5, 4, 4, 5, 3, 3, 2, 6, 1, 2, 1, 1, 6, 5]
#count_sixes = 0

#for result in dice_result:
#        if result == 1:
#                count_ones = count_ones + 1
#print("The number one was rolled:", count_ones, " times.")




dice_result = [5, 6, 4, 2, 5, 4, 4, 5, 3, 3, 2, 6, 1, 2, 1, 1, 6, 5]
consecutive_sixes = 0


for i in range(len(dice_result) - 1):
    if dice_result[i] == 6 and dice_result[i + 1] == 6:
        consecutive_sixes += 1

print("The number 6 was rolled consecutively", consecutive_sixes, "times.")