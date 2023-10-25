def average_age(hash_table):
    if not hash_table:
        return 0

    age_sum = 0
    total_students = 0

    for student, data in hash_table.items():
        age = int(data[1])
        age_sum += age
        total_students += 1

    return age_sum / total_students


hash_table = {}

with open('W3-EX3-input.txt', 'r') as file:
    for line in file:
        data = line.strip().split(';')

        if len(data) == 5:
            number, name, gender, age, phone_number = data

            if gender.upper() == 'F':
                hash_table[number] = [name, age, gender, phone_number]

for student, data in hash_table.items():
    print(f'{student} {data}')

value = input('Please enter an number: ')

if value in hash_table.keys():
    print(hash_table[value])
else:
    print('Not found!')

average = average_age(hash_table)
print(f'The average age is: {average:.2f}')
