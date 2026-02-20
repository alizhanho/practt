students = [
    {"name": "Islam", "grade": 89},
    {"name": "Nurka", "grade": 19},
    {"name": "Beka", "grade": 18}
]

# Sort by grade
sorted_students = sorted(students, key=lambda student: student["grade"])

print(sorted_students)