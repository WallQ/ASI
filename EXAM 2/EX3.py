import EX3Read as Read
import EX3Stats as Stats
import EX3List as List
import EX3ModifyInfo as ModifyInfo

grades_hash_table, student_names_hash_table = Read.read_file('EX3-input.txt')

for student_number, uc in grades_hash_table.items():
    print(f'Student Number: {student_number}')
    for uc, grade in uc.items():
        print(f'\tUC: {uc}, Grade: {grade}')

print('-' * 64)

average_grade_hash_table = Stats.average_grade(grades_hash_table)

for uc in average_grade_hash_table:
    print(f'UC: {uc}, Average Grade: {average_grade_hash_table[uc]:.2f}')

print('-' * 64)

List.list_hash_table(grades_hash_table, student_names_hash_table)

print('-' * 64)

ModifyInfo.modify_info(grades_hash_table)
