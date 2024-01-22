import EX4Read as Read
import EX4Investigate as Investigate

hash_table = Read.read_file('EX4-input.txt')

for drive_license, license_plate in hash_table.items():
    print(f'Driver License: {drive_license}')
    for license_plate, date in hash_table[drive_license].items():
        print(f'\tLicense Plate: {license_plate}')
        for date, infraction in hash_table[drive_license][license_plate].items():
            print(f'\t\tInfraction type: {infraction[0]}\n\t\tFine: {infraction[1]}\n\t\tDate Payment: {infraction[2]}\n')
    print('-' * 64)

print('-' * 64)

fines_hash_table = Investigate.calculate_fine_per_driver(hash_table)

for drive_license, fine in fines_hash_table.items():
    print(f'Driver License: {drive_license}\n\tTotal fines amount: {fine:.2f}€\n')