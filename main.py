from Auth import sign_up, sign_in


def main():
    user = sign_up()
    print(user)

    if sign_in(user):
        print('Authentication successful!')
    else:
        print('Authentication failed!')


if __name__ == '__main__':
    main()
