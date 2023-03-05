for _ in range(int(input())):
    n = int(input())
    s = input().lower()
    r = 'meow'
    i = 0
    prev = None
    for j in range(n):
        if s[j] == prev:
            continue
        elif i < 4 and s[j] == r[i]:
            i += 1
            prev = s[j]
        else:
            i = 0
            break
    print('YES' if i == 4 else 'NO')


