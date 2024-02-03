t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    zero = 0
    one = 0
    for i in range(n):
        if a[i] != b[i]:
            if a[i] == '0':
                zero += 1
            else:
                one += 1
    print(max(zero, one))