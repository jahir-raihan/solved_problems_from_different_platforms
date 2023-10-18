t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a[0] += 1

    s = a[0]
    for i in a[1:]:
        s *= i
    print(s)