from W4 import W4EX2Read as Read
from W4 import W4EX2Stats as Stats

hashTable = Read.read('W4-EX2-input.txt')

for url, visits in hashTable.items():
    print(f"URL: {url}")
    for data, details in visits.items():
        print(f"Data: {data}")
        for visit in details:
            print(f"Country: {visit['country']}, Duration: {visit['duration']}")

print('-' * 64)

url, visits = Stats.most_visited_url(hashTable)

print(f"Most visited URL: {url}, visits: {visits}")

print('-' * 64)

month_visits = Stats.month_with_most_visits(hashTable)

# {'12': 1, '01': 1, '02': 1}

# print the month with most visits
print(f"Month with most visits: {month_visits}")
