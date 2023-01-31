# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    i = a[-1]
    j = a[0]
    k = a[-2]

    print((i - j) * k)
