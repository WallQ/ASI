hash_table = {}
with open('EX1-input.txt', 'r') as file:
    for line in file:
        if line.startswith('#'):
            continue

        data = line.strip().split(';')

        if len(data) == 3:
            nif, license_plate, iuc = data

            if nif in hash_table:
                hash_table[nif][license_plate] = iuc
            else:
                hash_table[nif] = {license_plate: iuc}

for nif in hash_table.items():
    print(f'The NIF {nif[0]} has {len(nif[1])} vehicles.')

    total_iuc = 0
    for iuc in nif[1].items():
        total_iuc += float(iuc[1])

    print(f'The NIF {nif[0]} has to pay {total_iuc}€ IUC in total.')
