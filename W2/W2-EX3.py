from datetime import datetime


def classify_age(birthday):
    new_birthday = datetime.strptime(birthday, "%d/%m/%Y")

    current_age = 2021 - new_birthday.year

    if 0 <= current_age <= 12:
        return "Child"
    elif 13 <= current_age <= 17:
        return "Teenager"
    elif 18 <= current_age <= 64:
        return "Adult"
    else:
        return "Senior"


dates = ["12/08/2011", "21/06/1951", "05/06/2006", "03/01/1982", "21/05/2015"]

for date in dates:
    result = classify_age(date)
    print(f"{date} - {result}")
