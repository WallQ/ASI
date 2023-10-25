grades = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]

grade_occurrence = {}

for grade in grades:
    if grade in grade_occurrence:
        grade_occurrence[grade] += 1
    else:
        grade_occurrence[grade] = 1

print("Grade\tOccurrence")
for grade, occurrence in sorted(grade_occurrence.items()):
    print(f"{grade}\t{occurrence}")
