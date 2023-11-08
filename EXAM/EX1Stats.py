def total_sales(sales_hash_table):
    total_sales_per_isbn = {}
    total_sales = 0
    total_value_sales = 0

    for isbn, sales in sales_hash_table.items():
        if isbn not in sales_hash_table:
            sales_hash_table[isbn] = {}
        for sell_date, sales in sales.items():
            total_sales += len(sales)
            total_value_sales += float(sales[0][2])
        total_sales_per_isbn[isbn] = [total_sales, total_value_sales]

    return total_sales_per_isbn
