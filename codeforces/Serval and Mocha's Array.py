def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


for _ in range(int(input())):
    n = int(input())
    l = [int(num) for num in input().split()]
    x = 100000
    for i in range(n):
        for j in range(i + 1, n):
            gcd = find_gcd(l[i], l[j])
            if gcd < x:
                x = gcd
    print('NO' if x > 2 else 'YES')

