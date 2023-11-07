def read(filename):
    hash_table = {}

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue

            data = line.strip().split(';')

            if len(data) == 4:
                url, username, files, size = data

                if username in hash_table:
                    if url in hash_table[username]:
                        hash_table[username][url][0] += int(files)
                        hash_table[username][url][1] += float(size)
                    else:
                        hash_table[username][url] = [int(files), float(size)]
                else:
                    hash_table[username] = {url: [int(files), float(size)]}

    file.close()
    return hash_table
