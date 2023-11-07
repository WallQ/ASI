hash_table = {}
total_size = 0

report = open("report.txt", "w")

with open('EX2-input.txt', 'r') as file:
    for line in file:
        if line.startswith('#'):
            continue

        data = line.strip().split(' ')

        if len(data) == 2:
            name, bytes = data

            hash_table[name] = bytes

            total_size += int(bytes)

report.write("ASI Lda.\tDisk space usage by users\n")
report.write("-" * 64)
report.write('\n')
report.write("User\t\tDisk Space Used\t\t% Of Usage\n")

for user, bytes in hash_table.items():
    space_used = int(bytes) / 1024 / 1024
    percent = (float(bytes) / total_size) * 100
    report.write(f"{user}\t\t{space_used:.2f}MB\t\t{percent:.2f}%\n")

report.write('\n')
report.write(f"Total occupied space: {(total_size / 1024 / 1024):.2f}MB\n")
report.write(f"Average occupied space: {((total_size / (len(hash_table.keys()))) / 1024 / 1024):.2f}MB\n")
