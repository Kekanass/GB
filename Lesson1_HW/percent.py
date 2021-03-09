
count_percent = int(input('Введите значение:'))

r = list(range(5, 21))
if count_percent < 0:
    print('Введено недопустимое значение:')
elif count_percent == 0:
    print(count_percent, 'процентов')
elif count_percent == 1:
    print(count_percent, 'процент')
elif count_percent == 2 or count_percent == 3 or count_percent == 4:
    print(count_percent, 'процента')
elif count_percent in r :
    print(count_percent, 'процентов')
elif count_percent > 20:
    print('Введеное значение не отвечает условиям программы.')
else:
    print(count_percent)
