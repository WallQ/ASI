def list_hash_table(grades_hash_table, student_names_hash_table):
    approved_students = []

    for student_number, uc in grades_hash_table.items():
        for uc, grade in uc.items():
            if float(grade) >= 9.5 and uc == 'ASI':
                if student_number not in approved_students:
                    approved_students.append(student_number)

    for student_number, student_name in student_names_hash_table.items():
        if student_number in approved_students:
            print(f'{student_name} ({student_number}) is approved in ASI')
