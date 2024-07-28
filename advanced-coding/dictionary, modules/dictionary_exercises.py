# list
friends = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
print(friends)

# tuples
friends_tuples = [(friend, len(friend)) for friend in friends]
print(friends_tuples)

# My expenses
your_expenses = {
    'Clothes': 1100,
    'Shoes': 1000,
    'Watch': 900,
    'Mobile Recharge': 699,
    'Petrol': 1980
}

# Your wife's expenses
wife_expenses = {
    'Mobile Recharge': 799,
    'DTH recharge': 999,
    'Clothes': 2310,
    'Makeup': 3670,
    'Shoes': 999
}

# Calculating total expenses
total_your_expenses = sum(your_expenses.values())
print("My total expenses: ", total_your_expenses)
total_wife_expenses = sum(wife_expenses.values())
print("My total expenses: ", total_wife_expenses)

# Finding who is spending more
if total_your_expenses > total_wife_expenses:
    spender = "You are spending more"
    print(spender)
else:
    spender = "Your wife is spending more"
    print(spender)

# Finding the category of highest expenditure for each
max_your_expense_category = max(your_expenses, key=your_expenses.get)
max_wife_expense_category = max(wife_expenses, key=wife_expenses.get)
print(max_your_expense_category)
print(max_wife_expense_category)
