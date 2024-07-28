push_ups = [10, 10, 10, 10, 10]

status = 0
status2 = 50

for i in push_ups:
    if i == 10:
        status = status + i

    if status == 50:
        print("Congratulations! You made it!")
        break

    tired = input("Are you tired? (Y/N): ")

    if tired == "N":
        status2 = status2 - 10
        print(f"Remaining {status2} push-ups")

    elif tired == "Y":
        print(f"You did total of {status} push-ups")
        break
