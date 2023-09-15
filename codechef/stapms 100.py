t = int(input())
for _ in range(t):
    n = int(input())
    s = [i for i in input()]
    act = 0
    for j in range(n-2):
        if s[j] == '1':
            act = 1
            break
    if not act:
        print(s)
    else:
        print("0"*j + '1' + "0"*(n-j-1))
