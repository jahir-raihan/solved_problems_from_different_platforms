# cook your dish here

for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    res = 'YES'
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) > 1:
            res = 'NO'
            break
    print(res)
