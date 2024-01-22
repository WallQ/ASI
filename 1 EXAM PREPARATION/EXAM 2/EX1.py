import re

input = 'jpm@estgf.ipp.pt,mmo@aulas.pt,abc@gmail.com,abd@gmail.com'

pattern = re.compile(r'\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,7}\b')

emails = re.findall(pattern, input)

with open('EX1-output.txt', 'w') as output_file:
    for email in emails:
        output_file.write(email + '\n')
