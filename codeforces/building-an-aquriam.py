t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]

    l, r = 0, int(1e12)
    while l < r:
        mid = (l+r+1) // 2
        val = sum([max(0, mid - i) for i in a])
        if val > m:
            r = mid - 1
        else:
            l = mid
    print(l)



