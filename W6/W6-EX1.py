import re

inputs = [
    'Salt Cod with Chickpeas and Spinach: $6.137',
    'Alheira, Egg and Turnip Greens: $7.364',
    'Smoked Turkey Sandwich: $4.5001'
]

dollar_to_euro = 0.85

pattern = re.compile(r'^(.*):\s\$(.*)$')

for products in inputs:
    match = pattern.match(products)
    if match:
        name = match.group(1)
        price = float(match.group(2))
        new_price = price * dollar_to_euro
        print(f'{name}: ${price} -> €{new_price:.2f}')

