def thesaurus_sorted(*args):
    result = {}
    key_set = sorted({name[0].upper() for name in args})
    for item in key_set:
        new_list = []
        for name in args:
            if item == name[0].upper():
                new_list.append(name)
        result[item] = new_list
    return result


print(thesaurus_sorted("Иван", "Мария", "Петр", "Илья"))