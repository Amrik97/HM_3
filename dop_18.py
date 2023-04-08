def find(n, num):
    print()
    print(n)
    m = []

    for i in range(n):
        m.append(i + 1)

    s = ""
    res = 0
    for a in m:
        if a == num:
            res = a
        s += str(a) + " "

    if res == 0:
        res = m[len(m)-1]
    print(s)
    print(num)
    print("-> %d" % res)


if __name__ == '__main__':
    try:
        find(int(input("Введите количество элементов: \n")), int(input("Введите число: \n")))
    except ValueError:
        print("Вы ввели не числа!")
        exit(0)
