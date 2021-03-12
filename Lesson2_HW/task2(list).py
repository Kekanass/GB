forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i, el in enumerate(forecast):
    if el.count('+') > 0:
        if el.replace('+', '').isdigit():
            el = int(el)
            forecast[i] = f'"+{el:02d}"'
    elif el.count('-') > 0:
        if el.replace('-', '').isdigit():
            el = int(el)
            forecast[i] = f'"{el:03d}"'
    elif el.isdigit():
        el = int(el)
        forecast[i] = f'"{el:02d}"'
message = " ".join(forecast)
print(message)
