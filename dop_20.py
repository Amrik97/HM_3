list_en_1 = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "L", "l", "N", "n", "S", "s", "T", "t", "R", "r"]
list_en_2 = ["D", "d", "G", "g"]
list_en_3 = ["B", "b", "C", "c", "M", "m", "P", "p"]
list_en_4 = ["F", "f", "H", "h", "V", "v", "W", "w", "Y", "y"]
list_en_5 = ["K", "k"]
list_en_8 = ["J", "j", "X", "x"]
list_en_10 = ["Q", "q", "Z", "z"]

list_ru_1 = ["А", "а", "В", "в", "Е", "е", "И", "и", "Н", "н", "О", "о", "Р", "р", "С", "с", "Т", "т"]
list_ru_2 = ["Д", "д", "К", "к", "Л", "л", "М", "м", "П", "п", "У", "у"]
list_ru_3 = ["Б", "б", "Г", "г", "Ё", "ё", "Ь", "ь", "Я", "я"]
list_ru_4 = ["Й", "й", "Ы", "ы"]
list_ru_5 = ["Ж", "ж", "З", "з", "Х", "х", "Ц", "ц", "Ч", "ч"]
list_ru_8 = ["Ш", "ш", "Э", "э", "Ю", "ю"]
list_ru_10 = ["Щ", "щ", "Ъ", "ъ"]


def count(word):
    res = 0

    for a in word:
        if a in list_en_1 or a in list_ru_1:
            res += 1
        elif a in list_en_2 or a in list_ru_2:
            res += 2
        elif a in list_en_3 or a in list_ru_3:
            res += 3
        elif a in list_en_4 or a in list_ru_4:
            res += 4
        elif a in list_en_5 or a in list_ru_5:
            res += 5
        elif a in list_en_8 or a in list_ru_8:
            res += 8
        elif a in list_en_10 or a in list_ru_10:
            res += 10
        else:
            print("В слове присутсвуют посторонние символы!")
            exit(0)

    print(res)


if __name__ == '__main__':
    count(input("Введите слово: "))
    exit(0)
