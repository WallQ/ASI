def paid_most_imi(properties):
    nif_biggest_tax_imi = None
    biggest_tax_imi = 0.0

    for nif, propertie_data in properties.items():
        total_tax_imi_nif = sum(propertie_data.values())
        if total_tax_imi_nif > biggest_tax_imi:
            biggest_tax_imi = total_tax_imi_nif
            nif_biggest_tax_imi = nif

    return nif_biggest_tax_imi, biggest_tax_imi


def calc_taxes(vehicles, properties):
    taxes = {}

    for nif in vehicles.keys():
        taxes[nif] = 0.0

    for nif, vehicles_data in vehicles.items():
        for license_plate, iuc in vehicles_data.items():
            taxes[nif] += iuc

    for nif, properties_data in properties.items():
        for matrix_article, imi in properties_data.items():
            taxes[nif] += imi

    return taxes


vehicles_hash_table = {}
properties_hash_table = {}

with open('W3-EX4-input.txt', 'r') as file:
    for line in file:
        data = line.strip().split(';')

        if len(data) == 7:
            nif, year, license_plate, iuc, matrix_article, value, imi = data

            if license_plate:
                if nif not in vehicles_hash_table:
                    vehicles_hash_table[nif] = {}
                vehicles_hash_table[nif][license_plate] = float(iuc)

            if matrix_article:
                if nif not in properties_hash_table:
                    properties_hash_table[nif] = {}
                properties_hash_table[nif][matrix_article] = float(value)

print("Vehicles Hashtable:")
for nif, vehicles_data in vehicles_hash_table.items():
    print(f'NIF: {nif}')
    for license_plate, iuc in vehicles_data.items():
        print(f'License Plate: {license_plate}, IUC: {iuc}')

print('\n')

print("Properties Hashtable:")
for nif, properties_data in properties_hash_table.items():
    print(f'NIF: {nif}')
    for matrix_article, imi in properties_data.items():
        print(f'Matrix Article: {matrix_article}, IMI: {imi}')

print('\n')

nif_biggest_tax_imi, biggest_tax_imi = paid_most_imi(properties_hash_table)
print(f"The nif who paid the most TAX in 2018 was {nif_biggest_tax_imi} with a value of {biggest_tax_imi:.2f}.")

print('\n')

taxes = calc_taxes(vehicles_hash_table, properties_hash_table)
for nif, total_taxes in taxes.items():
    print(f"NIF: {nif}, Total taxes: {total_taxes}")
