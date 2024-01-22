from datetime import date
import re

type_proc_pattern = re.compile(r"[A-Z]{1}[a-z]+")
type_contract_pattern = re.compile(r"[A-Z]{1}[a-z]+", re.UNICODE)
cpv_pattern = re.compile(r"\d{8}-\d{1}")
ea_pattern = re.compile(r"[A-Z]{1}[a-z]+\s\(\d{9}\)", re.UNICODE)
eaj_pattern = re.compile(r"[A-Z]{1}[a-z]+\(\d{9}\)", re.UNICODE)
price_pattern = re.compile(r"(\d+\.)?\d{3},\d{2}\s€")  # Something wrong...
data_contact_pattern = re.compile(r"(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/\d{4}/")
term_pattern = re.compile(r"^(0?[1-9]|[12][0-9]|3[01])?$")

contract = input("Enter a contract: ")

data = contract.split(";")

if type_proc_pattern.match(data[0]) and type_contract_pattern.match(data[1]) and cpv_pattern.match(
        data[2]) and ea_pattern.match(data[3]) and eaj_pattern.match(data[4]) and price_pattern.match(
    data[5]) and data_contact_pattern.match(data[6]) and term_pattern.match(data[7]):

    print(f"Contract Valid!")

    today = date("09/11/2023")
    new_date = data[6].rstrip(data[6][-1])
    diffrence = today - date(new_date)

    if diffrence > 0:
        print(f"Contract expired!")

else:
    print(f"Contract Invalid!")
