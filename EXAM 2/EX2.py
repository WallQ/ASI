import re

input = 'Luis Corte-Real Sousa'

pattern = re.compile(r'\b\w')

initials = re.findall(pattern, input)

initials_formated = '.'.join(map(str.lower, initials))

print(initials_formated)
