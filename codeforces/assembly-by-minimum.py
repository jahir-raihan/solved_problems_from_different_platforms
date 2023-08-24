t = int(input())
for _ in range(t):
    n = int(input())
    b = sorted(map(int, input().split()))
    j = 0
    for i in range(n-1, 0, -1):
        print(b[j], end=' ')
        j += i
    print(b[-1])
