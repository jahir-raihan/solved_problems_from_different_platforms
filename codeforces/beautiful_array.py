def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if a[0] % 2 == 1:
        print("YES")
        return
    for i in range(n):
        if a[i] % 2 == 1:
            print("NO")
            return
    print("YES")


t = int(input())
for _ in range(t):
    solve()