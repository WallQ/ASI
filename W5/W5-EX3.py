import re


def number_of_lower_characters(phrase):
    pattern = re.compile(r'[a-z\s]*')

    return len(pattern.findall(phrase)[0])


phrase = input("Enter your phrase: ")

print("Number of lower characters: ", number_of_lower_characters(phrase))
