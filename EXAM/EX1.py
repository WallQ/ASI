from EXAM import EX1Read as Read
from EXAM import EX1Stats as Stats

hash_table = Read.read('EX1-input.txt')

for isbn, sell_dates in hash_table.items():
    print('ISBN: {}'.format(isbn))

    for sell_date, books in sell_dates.items():
        print('Sell date: {}'.format(sell_date))

        for book in books:
            print('Title: {}, Publisher: {}, Base price: {}, Discount: {}'.format(*book))

total_sales, total_value_sales = Stats.total_sales(hash_table)
