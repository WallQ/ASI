from W7 import Read
from W7 import Email


def print_data(data):
    for student_number, student_data in data.items():
        print(f'Student Number: {student_number}')
        for student in student_data:
            print(f'Name: {student["name"]}')
            print(f'Identity Card: {student["identity_card"]}')
            print(f'Birthday Date: {student["birthday_date"]}')
        print('-' * 64)


def main():
    data = Read.read_file('data')
    print_data(data)
    Email.send_email()

if __name__ == '__main__':
    main()
