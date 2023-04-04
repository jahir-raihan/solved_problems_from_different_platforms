for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())

    xor = 0
    for i in a:
        xor ^= i
    if n % 2 == 1:
        print(xor)
    else:
        print(xor if xor == 0 else -1)