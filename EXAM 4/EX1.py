import re

input = 'jpm@estgf.ipp.pt,mmo@aulas.pt,abc@gmail.com,abd@gmail.com'

patter = re.compile(r'\b[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z|A-Z]{2,7}\b')

emails = re.findall(patter, input)

with open("EX1-output.txt", "w") as file:
    for email in emails:
        file.write(email + '\n')
