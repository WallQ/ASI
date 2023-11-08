from datetime import datetime
from random import randint

from User import User


def sign_up():
    print('--- Sign Up ---')
    first_name = input('Insert first name: ')
    last_name = input('Insert last name: ')
    email = input('Insert email: ')
    password = input('Insert password: ')
    created_at = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    return User(randint(0, 100), first_name, last_name, email, password, created_at)


def sign_in(user):
    print('--- Sign In ---')
    email = input('Insert email: ')
    password = input('Insert password: ')

    if user.authenticate(email, password):
        return True
    else:
        return False
