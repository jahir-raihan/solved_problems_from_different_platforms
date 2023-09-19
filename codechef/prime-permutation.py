t = int(input())

for _ in range(t):
    n = int(input())

    if n <= 3:
        print(-1)
        continue
    ans = [i+1 for i in range(n)]

    for i in range(n - 2):
        if i % 4 <= 1:
            ans[i], ans[i + 2] = ans[i + 2], ans[i]

    if n % 4 == 1:
        ans[n - 1], ans[n - 3] = ans[n - 3], ans[n - 1]
        ans[n - 2], ans[n - 1] = ans[n - 1], ans[n - 2]

    elif n % 4 == 2:
        ans[n - 2], ans[n - 4] = ans[n - 4], ans[n - 2]
        ans[n - 1], ans[n - 3] = ans[n - 3], ans[n - 1]
        ans[n - 1], ans[n - 2] = ans[n - 2], ans[n - 1]

    elif n % 4 == 3:
        ans[n - 2], ans[n - 5] = ans[n - 5], ans[n - 2]

    print(*ans)