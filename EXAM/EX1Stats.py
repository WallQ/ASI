def total_sales(sales_hash_table):
    total_sales = 0
    total_value_sales = 0

    for i in range(len(sales_hash_table)):
        total_value_sales += sales_hash_table[i][1]
        total_sales += sales_hash_table[i][2]

    return total_sales, total_value_sales
