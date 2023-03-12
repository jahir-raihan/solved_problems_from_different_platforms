connections = [[1, 2], [2, 0], [0, 3], [3, 4], [7, 0], [7, 6], [7, 5]]
n = 6
adj_list = {i: [] for i in range(n)}
for k, v in connections:
    adj_list[k].append(v)
    adj_list[v].append(k)

visted = set()
visted.add(0)

