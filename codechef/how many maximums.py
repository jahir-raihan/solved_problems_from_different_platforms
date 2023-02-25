for _ in range(int(input())):
    n = int(input())
    s = input()
    res = 0 if s[-1] == '1' else 1
    prev = None
    for i in range(n - 1):
        if s[i] == '1' and prev != '1':
            res += 1
        prev = s[i]
    print(res)

