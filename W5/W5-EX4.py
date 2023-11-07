import re


def validate_full_name(full_name):
    pattern = re.compile(r'^[A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+(\s[A-Z]{1}[a-z]+)?(\s[A-Z][a-z]+)?$')

    if pattern.match(full_name):
        return True
    else:
        return False


full_name = input("Enter your full name: ")

if validate_full_name(full_name):
    print("Valid full name")
else:
    print("Invalid full name")