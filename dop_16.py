def find(n, num):
    print()
    print(n)
    m = []

    for i in range(n):
        m.append(i + 1)

    s = ""
    k = 0

    for a in m:
        if a == num:
            k += 1
        s += str(a) + " "

    print(s)
    print(num)
    print("-> %d" % k)


if __name__ == '__main__':
    try:
        find(int(input("Введите количество элементов: \n")), int(input("Введите число: \n")))
    except ValueError:
        print("Вы ввели не числа!")
        exit(0)
