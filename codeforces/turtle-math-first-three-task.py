t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)

    left = sum_a % 3
    if left > 0:
        left = (sum_a - left + 3) - sum_a
    removed = 2

    for i in a:
        if (sum_a - i) % 3 == 0:
            removed = 1
            break

    print(min(left, removed))





