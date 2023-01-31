for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    a = sorted([abs(i) for i in a])
    if a[0] == 0:
        print(-1)
    else:
        print(a[0]-1)