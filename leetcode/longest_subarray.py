lst = [2, 3, 4, 7]
l = [1, 3, 2]

for i in range(len(lst)):
    or_a = lst[:i+1]
    or_b = lst[i+1:]
    res = 0
    res_b = 0
    for ele in or_a:
        res = res | ele
    for ele in or_b:
        res_b = res | ele
    print()