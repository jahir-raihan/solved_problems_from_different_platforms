arr = [1, 1, 4]

res = set(arr)
itr = 0
for i in range(len(arr)):
    r = 0
    if arr[i] == arr[i - 1]:
        continue
    for j in range(i, len(arr)):
        r |= arr[j]
        res.add(r)
        itr += 1
print(len(res))
print(itr)