import re


def read(file_name):
    contracts_hash_table = {}
    date_pattern = re.compile(r"\b(0?[1-9]|[12][0-9]|3[01])\/(0?[1-9]|1[012])\/\d{4}\b")
    price_pattern = re.compile(r"(\d+\.)?\d+,\d{2}")

    with open(file_name, "r") as file:
        for line in file:
            if line.startswith("#"):
                continue

            data = line.strip().split(';')

            if len(data) == 8:
                product_type, contract_type, cpv, ea, eaj, price, contract_date, term = data

                if ea not in contracts_hash_table.keys():
                    contracts_hash_table[ea] = {}

                new_date = re.findall(date_pattern, contract_date)[0]
                new_date_formatted = new_date[0] + "/" + new_date[1]

                new_price = re.findall(price_pattern, price)[0]  # Something wrong...

                contracts_hash_table[ea][new_date_formatted] = (eaj, cpv, price, product_type)
                # contracts_hash_table[ea][new_date_formatted] = (eaj, cpv, float(new_price), product_type)

    return contracts_hash_table
