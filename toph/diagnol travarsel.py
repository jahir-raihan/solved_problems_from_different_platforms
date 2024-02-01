t = 1

for _ in range(t):
    n, x, y = 4, 6, 5

    need = n - (x // 2)
    if need <= 0:
        print("YES")
    else:

        got = 2 * need
        x -= got
        need = n - (x // 2)
        if x <= 0:
            print("NO")
        else:

            for i in range(y // 3):
                if got > 0:
                    need -= 1
                    got -= 1
            print("YES" if need <= 0 else "NO")