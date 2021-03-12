print(f'Выражение 15*3 имеет тип: {type(15*3)} и значение: {15*3} \n'
      f'Выражение 15/3 имеет тип: {type(15/3)} и значение: {15/3} \n'
      f'Выражение 15**3 имеет тип: {type(15**3)} и значение: {15**3} \n'
      f'Выражение 15//3 имеет тип: {type(15//3)} и значение: {15//3} \n')

#или


multiplication_type, multiplication = str(type(15*3)).split("'")[-2:-3:-1], 15*3
division_type, division = str(type(15/3)).split("'")[-2:-3:-1], 15/3
extent_type, extent = str(type(15**3)).split("'")[-2:-3:-1], 15**3
division_without_remainder_type, division_without_remainder = str(type(15//3)).split("'")[-2:-3:-1], 15//3

multiplication_type = str(multiplication_type).replace("'", "").replace("[", "").replace("]", "")
division_type = str(division_type).replace("'", "").replace("[", "").replace("]", "")
extent_type = str(extent_type).replace("'", "").replace("[", "").replace("]", "")
division_without_remainder_type = str(division_without_remainder_type).replace("'", "").replace("[", "").replace("]", "")

print(f'\n \nВыражение 15*3 имеет тип: {multiplication_type} и значение: {multiplication} \n'
      f'Выражение 15/3 имеет тип: {division_type} и значение: {division} \n'
      f'Выражение 15**3 имеет тип: {extent_type} и значение: {extent} \n'
      f'Выражение 15//3 имеет тип: {division_without_remainder_type} и значение: {division_without_remainder} \n')

#или

check_type_this = [15*3, 15/3, 15**3, 15//3]
for i in check_type_this:
    #print(check_type_this[i])
    print(f'Значение: {i} имеет тип: {type(i)}')
