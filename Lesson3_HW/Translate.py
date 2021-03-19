def num_translate(num_for_tranlate):
    num_en = {"one": "один", "two": "два", "three": "три",
              "four": "четыри", "five": "пять", "six": "шесть", "zero": "ноль",
              "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    for key, value in num_en.items():
        if key == num_for_tranlate:
            return value
        elif value == num_for_tranlate:
            return key


num_introduced = str(input("Введите значение для перевода:"))
print(num_translate(num_introduced))
