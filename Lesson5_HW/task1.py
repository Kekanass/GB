

def odd_nums (n):
    for el in range(1, n+1, 2):
        yield el


odd_to_n = odd_nums(15)
print(next(odd_to_n))     # вызываем на печать элементы генератора по почереди.
print(next(odd_to_n))
print(next(odd_to_n))
print(*odd_to_n)          # Показываем "остато" Генератора. Доказываем, что он истощился.



