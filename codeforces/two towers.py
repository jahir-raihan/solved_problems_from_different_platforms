
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input() + input()[::-1]
    cnt = 0
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            cnt += 1
        if cnt > 1:
            break
    print('YES' if cnt < 2 else 'NO')


