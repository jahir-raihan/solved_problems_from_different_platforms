i = input

for _ in range(int(i())):
    n, x = map(int, i().split())
    freshness_value_of_items = list(map(int, i().split()))
    cost_of_each_item = list(map(int, i().split()))
    res = 0
    for idx in range(len(freshness_value_of_items)):
        if freshness_value_of_items[idx] >= x:
            res += cost_of_each_item[idx]

    print(res)