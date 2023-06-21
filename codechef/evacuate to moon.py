t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())
    car_cap = [int(i) for i in input().split()]
    outlet_cap = [int(i) for i in input().split()]
    car_cap.sort(reverse=True)
    outlet_cap.sort(reverse=True)
    min_len = min(n, m)

    res = 0

    for i in range(min_len):
        res += min(car_cap[i], outlet_cap[i] * h)
    print(res)