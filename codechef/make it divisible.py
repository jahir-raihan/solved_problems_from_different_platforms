print(int('1'+'00'))

for _ in range(1):
    n = 3
    if n > 1:
        start = int('1' + '0' * (n - 1))
        while True:
            if start % 3 == 0 and start % 9 != 0 and start % 2 == 1:
                break
            start += 1
        print(start)