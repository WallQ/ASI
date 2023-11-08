def reward(hash_table):
    max_visits = 0
    max_username = None
    min_visits = 0
    min_username = None
    hash_table_visits = {}

    for url, usernames in hash_table.items():
        for username, total_time in usernames.items():
            if 'https://www.facebook.com/' in url:
                if username in hash_table_visits:
                    hash_table_visits[username] += 1
                else:
                    hash_table_visits[username] = 1

    for username, visits in hash_table_visits.items():
        if visits > max_visits:
            max_visits = visits
            max_username = username
        if visits < min_visits or min_visits == 0:
            min_visits = visits
            min_username = username

    hash_table_visits = {
        'good': {min_username: min_visits},
        'bad': {max_username: max_visits}
    }

    return hash_table_visits
