def read_file(file_name):
    grades_hash_table = {}
    student_names_hash_table = {}

    with open(file_name, 'r') as file:
        for line in file:
            if line.strip().startswith('#'):
                continue

            data = line.strip().split(';')

            if len(data) == 4:
                uc, student_number, name, grade = data

                if student_number not in grades_hash_table.keys():
                    grades_hash_table[student_number] = {}

                if student_number not in student_names_hash_table.keys():
                    student_names_hash_table[student_number] = name

                grades_hash_table[student_number][uc] = grade

    return grades_hash_table, student_names_hash_table
