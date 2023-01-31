for i in range(int(input())):
    lst = sum(list(map(int, input().split())))
    print('YES' if lst == 180 else 'NO')