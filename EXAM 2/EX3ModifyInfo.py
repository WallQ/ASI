import re


def modify_info(hash_table):
    pattern = re.compile(r'\d+')

    for student_number, uc in hash_table.items():
        print(f'Student Number: {student_number}')
        for uc, grade in uc.items():
            new_grade = re.sub(pattern, r'\1.0', grade)
            print(f'\tUC: {uc}, Grade: {new_grade}')
