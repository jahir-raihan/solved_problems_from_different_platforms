lst = [1,2,3,4]
for i in range(len(lst)):
    if i > 0:
        t = lst[i-1]
        lst[i] += t