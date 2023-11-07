def read(filename):
    hash_table = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue

            data = line.strip().split(';')

            if len(data) == 4:
                url, username, time, total_time = data

                if url in hash_table:
                    hash_table[url][username] = total_time
                else:
                    hash_table[url] = {username: total_time}

    file.close()
    return hash_table
