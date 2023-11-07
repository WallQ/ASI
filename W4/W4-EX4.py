from W4 import W4EX4Average as Average
from W4 import W4EX4Quota as Quota
from W4 import W4EX4Read as Read

hashTable = Read.read('W4-EX4-input.txt')

for username in hashTable:
    print(username)
    for url in hashTable[username]:
        print('- ' + url)
        print('     - ' + str(hashTable[username][url][0]))
        print('     - ' + str(hashTable[username][url][1]))
    print('-' * 64)

averageSize = Average.average_size(hashTable)

for url in averageSize:
    print(url + ': ' + str(averageSize[url]))

print('-' * 64)

quota = Quota.warning(hashTable)

for username in quota:
    print(username + ', you have exceeded your download quota by: ' + str(quota[username]) + 'MB')

print('-' * 64)
