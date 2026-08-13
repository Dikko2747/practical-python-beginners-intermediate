import json

students = [
    {"name": "Adaeze", "gpa": 4.5},
    {"name": "Bello", "gpa": 3.8},
]

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=2)

with open("students.json", encoding="utf-8") as f:
    data = json.load(f)

print(data)
