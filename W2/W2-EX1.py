ages = [16, 18, 10, 28, 24, 26, 30, 46, 72, 65, 91]

print(f'Minimum age: {min(ages)}')
print(f'Maximum age: {max(ages)}')
print(f'Average age: {sum(ages) / len(ages):.2f}')

ages_filtered = [age for age in ages if 18 <= age <= 65]
average = sum(ages_filtered) / len(ages_filtered)

print(f'Average age between 18 and 65: {average:.2f}')
