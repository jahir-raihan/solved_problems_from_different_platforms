t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    res = 'YES'
    for i in range(n-1):
        if a[i] > a[i+1] and i+1 not in (1, 2, 4, 8, 16):
            res = 'NO'
            break
    print(res)
