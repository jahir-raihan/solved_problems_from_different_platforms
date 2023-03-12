numCourses = 5
prerequisites = [[0,1],[0,2],[1,2],[1,3],[3,2]]
dic = {}

for ele in prerequisites:
    if ele[0] in dic:
        dic[ele[0]].append(ele[1])
    else:
        dic[ele[0]] = [ele[1]]

q = [k for k, v in dic.items()]
# Find for loops in Adjacency list with dictionary representation.
v = {}
ans = {'ans': True}

def dfs(ele, qu):
    if ele not in v and ele in dic:
        for sub_ele in dic[ele]:
            if sub_ele in qu:
                ans['ans'] = False
                return
            qu.append(sub_ele)
            dfs(sub_ele, qu)
    v[ele] = True
    qu.pop()


for e in q:
    if ans['ans']:
        dfs(e, qu=[e])
    else:
        break
print(ans['ans'])
