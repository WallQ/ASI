import EX3Read as Read
import EX3Stats as Stats
import EX3List as List

students_grades_hash_table, students_names_hash_table = Read.read_file('EX3-input.txt')

for student_number, uc in students_grades_hash_table.items():
    print(f'Student Number: {student_number}')
    for uc, grade in uc.items():
        print(f'\tUC: {uc}, Grade: {grade}')

print('-' * 64)

average_grade_hash_table = Stats.calculate_average_grade_per_uc(students_grades_hash_table)

for uc in average_grade_hash_table:
    print(f'UC: {uc}, Average Grade: {average_grade_hash_table[uc]:.2f}')

print('-' * 64)

List.list_students_with_approval(students_grades_hash_table, students_names_hash_table)

print('-' * 64)


