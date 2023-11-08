import re

pattern = re.compile(r'^\d{4}/(0?[1-9]|1[012])/(0?[1-9]|[12][0-9]|3[01])\s(0?[0-9]|[1][0-9]|[2][0-3]):(0?[0-9]|[12345][0-9]):(0?[0-9]|[12345][0-9])$')

date = input("Enter date: ")

if pattern.match(date):
    print("Valid Date")
else:
    print("Invalid Date")
