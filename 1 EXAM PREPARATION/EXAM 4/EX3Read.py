def read_file(file_name):
    students_grades_hash_table = {}
    students_names_hash_table = {}

    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue

            data = line.strip().split(';')

            if len(data) == 4:
                uc, student_number, name, grade = data

                if student_number not in students_grades_hash_table.keys():
                    students_grades_hash_table[student_number] = {}

                if student_number not in students_names_hash_table.keys():
                    students_names_hash_table[student_number] = name

                students_grades_hash_table[student_number][uc] = grade

    return students_grades_hash_table, students_names_hash_table
