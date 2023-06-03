for _ in range(int(input())):
    n, k = map(int, input().split())
    rem = 0
    count = 1
    if n % k != 0:
        print(1)
        print(n)
    else:
        while True:
            if n % k == 0:
                n -= 1
                rem += 1
            elif rem % k == 0:
                n -= 1
                rem += 1
            else:
                break
            count += 1
        print(count)
        print(n, rem)