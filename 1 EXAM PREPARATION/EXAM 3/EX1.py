import re

pattern = re.compile(r'\d{3}.\d{3}.\d{1}.\d{1}/\d{2}')

ip = input("Enter IP: ")

if pattern.match(ip):
    print("Valid IP")
else:
    print("Invalid IP")
