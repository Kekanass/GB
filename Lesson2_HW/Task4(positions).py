position_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in position_list:
    name = (i.split()[-1:-2:-1]).pop()
    name = str(name).title()
    print(f'Привет, {name}!')


