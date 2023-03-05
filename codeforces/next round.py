n, k = map(int, input().split())
s = list(map(int, input().split()))

sc = s[k - 1]
cnt = 0
for i in range(n):
    if s[i] < sc or s[i] < 1:
        break
    cnt += 1
print(cnt)
