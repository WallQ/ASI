import re


def validate_citizen_card(cardNumber):
    # Other pattern way ^\d{8}\s{1}\d{1}\s{1}[A-Z]{2}\d{1}$
    patter = re.compile(r'^[0-9]{8}\s{1}[0-9]{1}\s{1}[A-Z]{2}[0-9]{1}$')

    if patter.match(cardNumber):
        return True
    else:
        return False


cc = input("Enter your citizen card number: ")

if validate_citizen_card(cc):
    print("Valid citizen card number")
else:
    print("Invalid citizen card number")
