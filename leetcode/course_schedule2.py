numCourses = 7
prerequisites = [[1,0], [2,0], [2,3], [2,4], [3,1], [4,1], [5,1], [5,6]]

dic = {c: [] for c in range(numCourses)}
for crs, pre in prerequisites:
    dic[crs].append(pre)

v = {}
res = []
ans = {'ans': True}


def dfs(ele, qu):
    if ele not in v:
        for sub_ele in dic[ele]:
            if sub_ele in qu:
                ans['ans'] = False
                return
            qu.append(sub_ele)
            dfs(sub_ele, qu)

    va = qu.pop()
    if ele not in v:
        res.append(va)
        v[ele] = True


for e in range(numCourses):
    if ans['ans']:
        dfs(e, qu=[e])
    else:
        print([])
        break
print(res)

