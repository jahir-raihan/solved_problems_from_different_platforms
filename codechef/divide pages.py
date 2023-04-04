for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))

    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 1:
            alice += a[i]
        else:
            bob += a[i]
    print('YES' if alice % 2 == bob % 2 else 'NO')