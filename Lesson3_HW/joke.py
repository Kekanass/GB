from random import choice


def get_joke(words_1, words_2, words_3):
    """

    :param words_1: Первое слово нашей шутки, генерируется случайно функцией choice
    :param words_2: Второе слово нашей шутки, генерируется случайно функцией choice
    :param words_3: Третье слово нашей шутки, генерируется случайно функцией choice
    :return: Возвращает "шутку" из 3 случайных слов, заданных списков
    """
    for word_1, word_2, word_3 in zip(words_1, words_2, words_3):
        word_1 = choice(words_1)
        word_2 = choice(words_2)
        word_3 = choice(words_3)
        return f'{word_1}, {word_2}, {word_3}'


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_joke(nouns, adverbs, adjectives))
