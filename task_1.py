#1
list_1 = ['Зима', 'Весна', 'Лето', 'Осень']
if __name__ in '__main__':
    a = int(input('Введите номер месяца: '))
    match a:
        case 12 | 1 | 2:
            print(list_1[0])
        case 3 | 4 | 5:
            print(list_1[1])
        case 6 | 7 | 8:
            print(list_1[2])
        case 9 | 10 | 11:
            print(list_1[3])
        case _:
            print('Нет такого месяца')

#2
my_dict = {'Зима': (12, 1, 2),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

if __name__ == '__main__':
    a = int(input('Введите номер месяца: '))
    if a in my_dict['Зима']:
        print("Зима")
    if a in my_dict['Весна']:
        print("Весна")
    if a in my_dict['Лето']:
        print("Лето")
    else:
        print("Осень")