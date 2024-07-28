India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

ask1 = input("Enter the name of a city: ")

if ask1 in India:
    print("The city is in India.")
elif ask1 in USA:
    print("The city is in USA.")
elif ask1 in UK:
    print("The city is in UK.")