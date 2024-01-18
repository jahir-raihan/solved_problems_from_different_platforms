from collections import defaultdict
t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    adj_lst = defaultdict(list)

    for _ in range(n):
        u, v = map(int, input().split())
        adj_lst[u].append(v)
        adj_lst[v].append(u)

    if a == b:
        print('NO')
        continue




