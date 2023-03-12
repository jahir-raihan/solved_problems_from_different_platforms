creators = ["alice", "bob", "alice", "chris"]
ids = ["one", "two", "three", "four"]
views = [5, 10, 5, 4]

total_list = {}
res = {}
mx = 0
for i, j, k in zip(creators, ids, views):
    if i in total_list:
        total_list[i] += k
    else:
        total_list[i] = k
    if i in res:
        res[i].append((j, k))
    else:
        res[i] = [(j, k)]

mxv = 0
res_ls = []
for k, v in total_list.items():
    if v > mxv:
        mxv = v
for k, v in total_list.items():
    if v == mxv:
        res_ls.append(k)

f_res = []
for itm in res_ls:
    tmp = res[itm]
    mx_v = -1
    mx_s = None
    for v, i in tmp:

        if i > mx_v:
            mx_v = i
            mx_s = v
        elif i == mx_v and v < mx_s:
            mx_s = v

    f_res.append([itm, mx_s])
print(f_res)