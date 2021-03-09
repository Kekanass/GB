
duration = int(input('Ввесдите значение в секундах:'))

if duration < 0:
    print('Введено недопустимое значение:')
elif duration == 0:
    print(duration, 'sec')
elif duration >= 60:
    minutes = duration // 60
    sec = duration % 60
    print(f'{minutes} :min, {sec} :sec')
    if minutes > 60:
        hours = minutes // 60
        minutes = minutes % 60
        print(f'{hours} :hours, {minutes} :min, {sec} :sec')
        if hours > 24:
            days = hours // 24
            hours = hours % 24
            print(f'{days} :days, {hours} :hours, {minutes} :min, {sec} :sec')
            if days > 30:
                mouth = days // 30
                days = days % 30
                print(f'{mouth} :mouth, {days} :days, {hours} :hours, {minutes} :min, {sec} :sec')
else:
    print(duration, 'sec')
