from sys import stdin, stdout
i = stdin.readline
res = []
for _ in range(int(i())):
    n = int(i())
    dic = {}
    sc = [int(s) for s in i().split()]
    q = int(i())
    for j in range(q):
        qu = [int(x) for x in i().split()]
        if qu[0] == 1:
            x, y = qu[1], qu[2]
            if x == y or (x == 0 or y == 0):
                continue
            if sc[x - 1] > sc[y - 1]:
                y, x = x, y

            sc[y - 1] += sc[x - 1]
            sc[x - 1] = 0
            try:
                dic[y - 1][1] += dic[x - 1][1]
                dic[x - 1][0] = y
                dic[x - 1][1] = 0
            except:
                dic[y - 1] = [y-1, 1]
                dic[x - 1] = [x-1, 1]
                dic[y - 1][1] += dic[x - 1][1]
                dic[x - 1][0] = y
                dic[x - 1][1] = 0

        elif qu[0] == 2:
            try:
                res.append(str(dic[qu[1] - 1][1]))
            except:
                res.append('1')
        elif qu[0] == 3:
            try:
                res.append(str(dic[qu[1] - 1][0]))
            except:
                res.append(str(qu[1]))
stdout.write('\n'.join(res))

