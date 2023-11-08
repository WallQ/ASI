import re


def total_sales(hash_table):
    isbn_sales = {}
    total_sales = 0
    total_value_sales = 0

    for isbn, sales in hash_table.items():
        if isbn not in isbn_sales:
            isbn_sales[isbn] = {}
        for sell_date, sales in sales.items():
            for sale in sales:
                total_sales += 1
                new_base_price = float(re.findall(r'\d*\.[0-9]{2}', sale[2])[0])
                total_value_sales += new_base_price
        isbn_sales[isbn] = [total_sales, total_value_sales]

    return isbn_sales
