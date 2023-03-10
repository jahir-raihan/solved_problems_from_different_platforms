
#   Naive approach

for _ in range(int(input())):
    n = int(input())
    dic = {}
    s = input()
    res = 0
    i, j = 0, 1
    while j < n:
        tmp = hash(s[:i] + s[j+1:])
        try:
            t = dic[tmp]
        except:
            dic[tmp] = 1
            res += 1

        i = j
        j = i + 1
    print(res)

#   Efficient Approach

for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    j = 2
    lst = []
    cnt = 1
    for k in range(2, n):
        lst.append(s[k])
    while j < n:
        if lst[j-2] != s[i]:
            cnt += 1
        lst[j-2] = s[i]

        i += 1
        j += 1
    print(cnt)
