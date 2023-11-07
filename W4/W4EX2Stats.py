def most_visited_url(hash_table):
    max_visits = 0
    max_url = None
    for url, visits in hash_table.items():
        if len(visits) > max_visits:
            max_visits = len(visits)
            max_url = url
    return max_url, max_visits


def month_with_most_visits(hash_table):
    max_month = {}

    for url, visits in hash_table.items():
        for data, details in visits.items():
            date = data.split('/')
            month = date[1]
            if month in max_month.items():
                max_month[month] += 1
            else:
                max_month[month] = 1
    return max_month
