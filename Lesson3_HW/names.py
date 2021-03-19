def create_names_dictionary(names):
    dictionary = {}
    for i in names:
        key = i.split()[:2:1]
        dictionary[key].append(i)
    return  dictionary


thesaurus = ("Иван", "Мария", "Петр", "Илья", "Александр", "Николай", "Алексей", "Олег", "Дмитрий")

print(create_names_dictionary(thesaurus))
