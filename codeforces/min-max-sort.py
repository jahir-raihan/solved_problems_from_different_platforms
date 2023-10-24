t = int(input())

for _ in range(t):
    n = int(input())
    a = [i for i in range(n+1)]
    lst = [int(i) for i in input().split()]
    for i in range(n):
        a[lst[i]] = i
    l, r = (n+1)//2, (n+2)//2

    while l > 0 and (l == r or (a[l] < a[l+1] and a[r-1] < a[r])):
        l -= 1
        r += 1
    print((n - r + l + 1) // 2)
