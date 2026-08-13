scores = [45, 72, 58, 90, 33, 66]

passed = [s for s in scores if s >= 50]
curved = [min(s + 5, 100) for s in scores]

people = [("Ada", 4.5), ("Ben", 3.8)]
top = sorted(people, key=lambda p: p[1], reverse=True)

print("Passed:", passed)
print("Curved:", curved)
print("Top:", top)
