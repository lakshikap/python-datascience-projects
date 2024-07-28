India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

ask1 = input("Enter the name of a city: ")
ask2 = input("Enter the name of another city: ")

if ask1 in India and ask2 in India:
    print("Both cities are in India.")
elif ask1 in USA and ask2 in USA:
    print("Both cities are in USA.")
elif ask1 in UK and ask2 in UK:
    print("Both cities are in UK.")
else:
    print("They don't belong to the same country.")