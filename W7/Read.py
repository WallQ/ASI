def read_file(file_name):
    hash_table = {}

    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            if line.strip().startswith('#'):
                continue

            data = line.strip().split(';')

            if len(data) == 4:
                student_number, name, identity_card, birthday_date = data

                if student_number not in hash_table:
                    hash_table[student_number] = []

                if len(hash_table[student_number]) == 0:
                    hash_table[student_number].append({
                        'name': name,
                        'identity_card': identity_card,
                        'birthday_date': birthday_date
                    })

    return hash_table
