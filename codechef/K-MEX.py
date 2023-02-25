
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    lst = [int(i) for i in input().split()]
    if n - lst.count(k) < m or k > m:
        print('NO')
    else:
        flag = True
        for i in range(k):
            if i not in lst:
                flag = False
                break
        print('YES' if flag else 'NO')







