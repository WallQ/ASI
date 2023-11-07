def read(file_name):
    sales_hash_table = {}

    with open('EX1-input.txt', 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue

            data = line.strip().split(';')

            if len(data) == 6:
                isbn, title, publisher, base_price, discount, sell_date = data

                if isbn in sales_hash_table:
                    sales_hash_table[isbn] = {}

                if sell_date not in sales_hash_table[isbn]:
                    sales_hash_table[isbn][sell_date] = []

                sales_hash_table[isbn][sell_date].append((title, publisher, base_price, discount))

    return sales_hash_table
