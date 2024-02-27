t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    res = 0
    for i in a:
        res += abs(i)
    print(res)