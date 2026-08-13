student = {"name": "Musa", "scores": [70, 82]}
student["dept"] = "CS"

for key, value in student.items():
    print(key, "→", value)

avg = sum(student["scores"]) / len(student["scores"])
print("Average:", avg)
