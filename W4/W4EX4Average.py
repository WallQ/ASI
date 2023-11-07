def average_size(hash_table):
    hash_table_average = {}

    for username in hash_table:
        for url in hash_table[username]:
            if url in hash_table_average:
                hash_table_average[url] += hash_table[username][url][1]
            else:
                hash_table_average[url] = hash_table[username][url][1]

    for url in hash_table_average:
        hash_table_average[url] /= len(hash_table)

    return hash_table_average
