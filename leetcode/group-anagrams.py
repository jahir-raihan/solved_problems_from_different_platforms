
strs = ["eat","tea","tan","ate","nat","bat"]
loc = {}
res = []

cnt = 0
for w in strs:
    try:
        l = loc[''.join(sorted(w))]
        res[l].append(w)
    except:
        loc[''.join(sorted(w))] = cnt
        res.append([w])
        cnt += 1
print(res)