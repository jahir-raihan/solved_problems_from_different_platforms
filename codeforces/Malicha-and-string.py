from collections import Counter

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    cnt = {'B': 0, 'A': 0}
    for i in s: cnt[i] += 1
    if cnt['B'] > m:
        i = 0
        while cnt['B'] > m:
            if s[i] == 'B':
                cnt['B'] -= 1
            i += 1
        print(1)
        print(i, 'A')
    elif cnt['B'] < m:
        i = 0
        while cnt['B'] < m:
            if s[i] == 'A':
                cnt['B'] += 1
            i += 1
        print(1)
        print(i, 'B')
    else:
        print(0)



   