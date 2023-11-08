import re

def calculate_fine_per_driver(hash_table):
    fine_per_driver = {}
    fine_pattern = re.compile(r'\d+.?\d+')

    for drive_license, license_plate in hash_table.items():
        for license_plate, date in hash_table[drive_license].items():
            sum_fine = 0.0
            for date, infraction in hash_table[drive_license][license_plate].items():
                sum_fine += float(fine_pattern.findall(infraction[1])[0])
            if drive_license not in fine_per_driver:
                fine_per_driver[drive_license] = sum_fine

    return fine_per_driver
