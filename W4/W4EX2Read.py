def read(filename):
    URLhashTable = {}
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(';')

            if len(data) == 4:
                url, date, country, time = data

                if url not in URLhashTable:
                    URLhashTable[url] = {}

                if date not in URLhashTable[url]:
                    URLhashTable[url][date] = []

                URLhashTable[url][date].append({'country': country, 'duration': time})
    file.close()
    return URLhashTable
