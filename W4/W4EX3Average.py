def time_string_to_seconds(time_string):
    h, m, s = map(int, time_string.split(':'))
    return h * 3600 + m * 60 + s


def average_time(hash_table):
    total_seconds = 0
    total_visits = 0
    hash_table_visits = {}

    for url, usernames in hash_table.items():
        for username, user_total_time in usernames.items():
            total_seconds += time_string_to_seconds(user_total_time)
            total_visits += 1
            hash_table_visits[url] = total_seconds / total_visits

    return hash_table_visits
