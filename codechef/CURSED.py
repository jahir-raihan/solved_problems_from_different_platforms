from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = [arr[0]]
    s = ans[0]
    new = arr.copy()
    while new:
        a = new.pop(0)
        if a>s:
            ans += [a]
            s += a
    print(n-len(ans))
    C = Counter(ans)
    for i in arr:
        if C[i]:
            C[i] -= 1
        else:
            ans += [i]
    print(*ans)