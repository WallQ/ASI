from EXAM import EX1Read as Read
from EXAM import EX1Stats as Stats

hash_table = Read.read('EX1-input.txt')

for isbn, sales in hash_table.items():
    print(f'ISBN -> {isbn}')
    for sell_date, sales in sales.items():
        print(f'\tSell Date: {sell_date} - Title: {sales[0][0]} - Publisher: {sales[0][1]} - Discount Price: {sales[0][2]}')
    print('-' * 64)

sales_per_isbn = Stats.total_sales(hash_table)

for isbn in sales_per_isbn:
    print(f'ISBN: {isbn} - Total Sales: {sales_per_isbn[isbn][0]} - Total Value Sales: {sales_per_isbn[isbn][1]:.2f}€.')