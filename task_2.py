def division(a,b):
    if b == 0:
        print("Вы что? Пытаетесь делить на 0!")
        exit(0)
    result = a / b
    print(result)

if __name__ == '__main__':
    try:
        division(int(input("Введите первое число: \n")), int(input("Введите второе число: \n")))
    except ValueError:
        print("Вы ввели не числа!")
        exit(0)