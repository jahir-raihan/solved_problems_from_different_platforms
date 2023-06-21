n = int(input())
vs = {}
lst = []
for _ in range(n):
    lst.append(input())
res = ''
for i in range(n-1, -1, -1):
    s = lst[i][-2:]
    try:
        tmp = vs[lst[i]]
    except:
        vs[lst[i]] = 0
        res += s
print(res)