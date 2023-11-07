def reward(hash_table):
    max_visits = 0
    max_username = None
    min_visits = 0
    min_username = None
    hash_table_visits = {}

    # Page Visited;Username;Timestamp;Total time visited
    # www.example.com;User1;2017 Mar 03 05:12:41.211 PDT; 00:01:34
    # hashtable = {url: {username: total_time}}
    # return the Username with the shortest number of visits to Facebook and print a
    # congratulation on the screen (ex: "Employee of the month: <Username>")
    # return the Username with the longest total time spent on Facebook and print a
    # message on the screen (ex: "<Username> you do need to focus more on your work")
    # hash_table_visits = {username: visits} <- max visits user & min visits user

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
