t = int(input())

for _ in range(t):
    s = input()+' '
    min_operation = 0
    b = 1
    c = 1
    for i in range(len(s)-1):
        if s[i] == s[i-1]:
            b = b * (min_operation + 1) % 998244353
            min_operation += 1
            c += 1
        else:
            b = b*c % 998244353
            c = 1
    print(min_operation, b * c % 998244353)


