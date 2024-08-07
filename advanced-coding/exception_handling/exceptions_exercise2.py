employees = [
    {"id": 1, "first_name": "John", "middle_name": "A.", "last_name": "Doe"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith"}
]
try:
    for employee in employees:
        full_name = employee['first_name'] + employee['middle_name'] + employee['last_name']
        print(full_name)
except KeyError as ke:
    print("Exception: Part of name is missing", ke)

