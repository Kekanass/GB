from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Василий', 'Аркадий'
]
klass = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

rez_generate = ((i, j) for i, j in zip_longest(tutors, klass, fillvalue=None))

print(next(rez_generate))
print(next(rez_generate))
print(next(rez_generate))
print(*rez_generate)




