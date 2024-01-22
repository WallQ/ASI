import datetime
import re


def calculate_prize(base_salary, employee_since_date, performance_indicator):
    base_salary = float(base_salary.replace('€', ''))
    print(f'BASE SALARY {base_salary}')
    employee_since_date = int(employee_since_date)
    performance_indicator = float(performance_indicator.replace('%', '')) / 100

    date_difference = datetime.date.today().year - int(employee_since_date)

    if date_difference <= 3:
        return (base_salary * 0.6) * performance_indicator
    elif 3 < date_difference <= 10:
        return (base_salary * 0.8) * performance_indicator
    elif date_difference > 10:
        return (base_salary * 1) * performance_indicator
    else:
        return 0


inputs = [
    'Ana Maria de Almeida e Santos;1000€;03/02/2020;90%',
    'Joao Pedro de Sousa;1800€;12/12/2007;100%',
    'Marinela Santos e Silva de Sousa;1400€;06/05/2015;90%',
]

for line in inputs:
    data = re.split(r';', line)

    name = data[0]
    salary = data[1]
    date = data[2].split('/')[2]
    indicator = data[3]

    new_date = datetime.date.today().year - int(date)

    prize = calculate_prize(salary, date, indicator)
    print(f'The employee {name} with a salary of {salary} with {new_date} years old on the company with a '
          f'performance'
          f'indicator of {indicator} got a prize of {prize}€.')
