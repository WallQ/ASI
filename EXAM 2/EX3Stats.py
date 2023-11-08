def average_grade(hash_table):
    average_grade_hash_table = {}

    for student_number, uc in hash_table.items():
        for uc, grade in uc.items():
            if uc not in average_grade_hash_table:
                average_grade_hash_table[uc] = []

            average_grade_hash_table[uc].append(grade)

    for uc, grades in average_grade_hash_table.items():
        sum_grades = 0
        for grade in grades:
            sum_grades += float(grade)
        average_grade_hash_table[uc] = sum_grades / len(grades)

    return average_grade_hash_table
