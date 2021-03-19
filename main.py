roster = list(range(1, 1001, 2)) # создаем список от 1 до 100, из нечетных чисел.
check_division = 1     # Проверка целочисленного деления, потребуется при сложении цифр числа.
counter_digits = 0     # значение суммы цифр числа
not_use = []         #список неинтересующих нас элементов списка
summ = 0             #сумма чисел списка, которые делятся на 7
roster_increased = list(range(1, 1001, 2))
not_use_increased = []
summ_increased = 0

for i in range(0, len(roster)):         #Пробегаем по списку
    check_division = roster[i] ** 3     # возводим элементы списка в куб и сразу присваиваем их для проверки
    while check_division != 0:           # т.к. мы не знаем трех значное чило, двух или больше, высчитываем сумму цифр в цикле
        counter_digits += check_division % 10
        check_division = check_division // 10
    roster[i] = counter_digits
    counter_digits = 0
    if (roster[i] % 7) != 0:                    # Проверяем делится ли чило целочисленно на 7
        not_use.append(roster[i])   # составляем список элементов, которые исключим, т.к. они не делятся на 7

for element in not_use:                             # исключаем элементы
        roster.remove(element)

for i in roster:                               # подсчитываем сумму элементов.
    summ += roster[i]


#По аналогии, только со списком, элементы которого увеличены на 17.

for i in range(0, len(roster_increased)):
    check_division = (roster_increased[i] ** 3) + 17
    while check_division != 0:
        counter_digits += check_division % 10
        check_division = check_division // 10
    roster_increased[i] = counter_digits
    counter_digits = 0
    if (roster_increased[i] % 7) != 0:
        not_use_increased.append(roster_increased[i])


for element in not_use_increased:                             # исключаем элементы
        roster_increased.remove(element)

for i in roster_increased:                               # подсчитываем сумму элементов.
    summ_increased += roster_increased[i]

print(summ_increased)
print(summ)
