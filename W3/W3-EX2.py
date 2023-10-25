hash_table = {}

with open('W3-EX2-input.txt', 'r') as file:
    for line in file:
        data = line.strip().split(';')

        if len(data) == 3:
            nif, license_plate, iuc = data
            if nif not in hash_table:
                hash_table[nif] = {}
            hash_table[nif][license_plate] = iuc

print(hash_table)

value = input('Please enter an NIF: ')

if value in hash_table.keys():
    print(hash_table[value])
else:
    print('Not found!')
