def my_func_sort(a, b, c):
    m = [a, b, c]
    m.sort()
    print(m[len(m) - 1] + m[len(m) - 2])


def my_func_2(a, b, c):
    if (a + b) > (a + c) and (a + b) > (b + c):
        print(a + b)
    elif (a + c) > (a + b) and (a + c) > (b + c):
        print(a + c)
    else:
        print(b + c)

