hash_table = {}

with open('W3-EX1-input.txt', 'r') as file:
    for line in file:
        data = line.strip().split(';')

        if len(data) == 5:
            number, name, gender, age, phone_number = data
            hash_table[number] = name

print(hash_table)

value = input('Please enter a number: ')

if value in hash_table.keys():
    print(hash_table[value])
else:
    print('Not found!')
