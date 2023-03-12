n = 3
for i in range(1, n + 1):
    if i == 1:

        s = ''
        for val in range(1, n + 1):
            s = s + str(val)
        print(s)
    elif i == n:
        s = ''
        for val in range(n, 0, - 1):
            s = s + str(val)
        print(s)

    else:
        if n > 3:
            print(i, (n - 4)*' ', n - i + 1)
        else:
            print(i, n - i + 1)
