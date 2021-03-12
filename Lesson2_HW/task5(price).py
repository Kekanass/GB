price = [12.35, 125.23, 154, 65.86, 78.25, 75.45, 24.32, 56, 86, 15.26, 6.32, 13.5, 1546.26]
print(id(price))
print(price)

price.sort()
print(id(price))
print(price)

a = []
for i, el in enumerate(price):
    a.append(f'{el*100//100:02.0f} рублей {(el*100%100):0.0f} копеек')
print(a)

price_max_min = sorted(price, reverse=True)
b = []
for i, el in enumerate(sorted(price_max_min[:5:], reverse=False)):
    b.append(f'{el*100//100:02.0f} рублей {(el*100%100):0.0f} копеек')
print(b)







