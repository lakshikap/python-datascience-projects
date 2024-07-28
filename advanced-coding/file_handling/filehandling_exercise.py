import csv

with open('student_marks.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Create a dictionary from the given data
    students_data = {}
    for row in reader:
        for key, value in row.items():
            if key not in students_data:
                students_data[key] = []
            students_data[key].append(value)

# Add a new field to the dic
total_marks = []
subjects = ['Maths', 'Physics', 'Chemistry', 'English', 'Biology', 'Economics', 'History', 'Civics']
for i in range(len(students_data[''])):
    total = sum(int(students_data[subject][i]) for subject in subjects if students_data[subject][i])
    total_marks.append(total)
students_data['total_marks'] = total_marks
print(total_marks)

# Add new field to the dic
average_marks = [total / len(subjects) for total in total_marks]
students_data['average_marks'] = average_marks

# Create a new file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    header = list(students_data.keys())
    writer.writerow(header)

    for i in range(len(students_data[''])):
        row = [students_data[key][i] for key in header]
        writer.writerow(row)

print("Data processing and writing to output.csv completed.")
