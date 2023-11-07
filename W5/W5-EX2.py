import re

male_dictionary = {}
female_dictionary = {}

pattern_male = re.compile(r';M;')
pattern_female = re.compile(r';F;')

with open('W5-EX2-input.txt', 'r') as file:
    for line in file:
        data = line.strip()

        if pattern_male.search(line):
            data = line.strip().split(';')

            if len(data) == 4:
                name, age, gender, phone = data

            new_phone = '00351' + phone

            male_dictionary[new_phone] = name
        elif pattern_female.search(line):
            data = line.strip().split(';')

            if len(data) == 4:
                name, age, gender, phone = data

            new_phone = '00351' + phone
            
            female_dictionary[new_phone] = name

print(male_dictionary.items())
print(female_dictionary.items())
