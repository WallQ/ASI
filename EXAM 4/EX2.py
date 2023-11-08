import re

input = 'Luis Corte-Real Sousa'

pattern = re.compile(r'\b\w')

initials = re.findall(pattern, input)

intials_formated = '.'.join(initials)

print(intials_formated.lower())