from W4 import W4EX3Average as Average
from W4 import W4EX3Read as Read
from W4 import W4EX3Reward as Reward

hashTable = Read.read('W4-EX3-input.txt')

for url, usernames in hashTable.items():
    print(f"URL: {url}")
    for username, total_time in usernames.items():
        print(f"Username: {username}, Total time: {total_time}")
    print('-' * 64)

average_time = Average.average_time(hashTable)

for url, average_time in average_time.items():
    print(f"URL: {url}, Average time: {average_time:.2f}")

print('-' * 64)

user_time = Reward.reward(hashTable)

for good_bad, usernames in user_time.items():
    for username, visits in usernames.items():
        if good_bad == 'good':
            print(f"Employee of the month: {username} with {visits} visit(s)")
        else:
            print(f"{username} you do need to focus more on your work, you visited Facebook {visits} time(s)")

print('-' * 64)
