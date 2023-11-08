def read_file(file_name):
    drivers_hash_table = {}

    with open(file_name, 'r') as file:
        for line in file:
            if line.strip().startswith('#'):
                continue

            data = line.strip().split(';')

            if len(data) == 6:
                drive_license, license_plate, date, infraction, fine, date_payment = data

                if drive_license not in drivers_hash_table:
                    drivers_hash_table[drive_license] = {}

                if license_plate not in drivers_hash_table[drive_license]:
                    drivers_hash_table[drive_license][license_plate] = {}

                drivers_hash_table[drive_license][license_plate][date] = [infraction, fine, date_payment]

    return drivers_hash_table
