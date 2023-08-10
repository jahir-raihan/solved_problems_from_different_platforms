for cas in range(int(input())):
    input()
    a = list(map(int, input().split()))
    if min(a) + max(a.count(1) - 1, 0) + len(a) <= sum(a):
        print('YES')
    else:
        print('NO')