def warning(hash_table):
    hash_table_exceeded = {}

    for username in hash_table:
        total_size = 0
        for url in hash_table[username]:
            total_size += hash_table[username][url][1]
        if total_size > 100:
            hash_table_exceeded[username] = total_size

    return hash_table_exceeded
