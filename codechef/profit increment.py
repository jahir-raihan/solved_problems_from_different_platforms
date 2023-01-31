# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    amount_with_profit = int(10 / 100 * a) + a
    res = amount_with_profit - (a - b)
    print(res)

