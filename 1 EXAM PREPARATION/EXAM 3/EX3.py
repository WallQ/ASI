import re
from datetime import datetime

input = 'Jose Maria Almeida;00351 962341234;1997-12-19'

data = input.split(';')

name_pattern = re.compile(r'^[A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+(\s[A-Z]{1}[a-z]+)?(\s[A-Z]{1}[a-z]+)?$')
phone_pattern = re.compile(r'^00351\s\d{9}$')
date_pattern = re.compile(r'\d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])')

if name_pattern.match(data[0]) and phone_pattern.match(data[1]) and date_pattern.match(data[2]):
    age = datetime.today().year - datetime.strptime(data[2], '%Y-%m-%d').year

    print(f'Name: {data[0]}, Phone: {data[1]}, Date: {data[2]}, in 2023 will be {age} years old.')
else:
    print('Invalid data!')

