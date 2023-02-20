for _ in range(int(input())):
    a, b = map(int, input().split())
    if b > a:
        if b % a == 0:
            print(1)
        else:
            print(a)
    else:
        if a % b == 0:
            print(a // b)
        elif a % 2 == 1:
            print(a)
        else:
            cnt = 1
            tmp = b
            while tmp % a != 0:
                tmp += b
                cnt += 1
            print(cnt)