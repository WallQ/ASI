def read_file(file_name):
    hash_table = {}

    with open(file_name, 'r') as file:
        for line in file:
            if line.strip().startswith('#'):
                continue

            data = line.strip().split(';')

            if len(data) == 6:
                isbn, title, publisher, base_price, discount, sale_date = data

                if isbn not in hash_table.keys():
                    hash_table[isbn] = {}

                if sale_date not in hash_table[isbn].values():
                    hash_table[isbn][sale_date] = []

                hash_table[isbn][sale_date].append((title, publisher, base_price, discount))

    return hash_table
