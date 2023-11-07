basePrice = float(input('Enter a value: '))

finalPrice = f"({basePrice}*23/100)-10"

result = eval(finalPrice)

print(f'The final price is: {result}')
