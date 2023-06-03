n = int(input())
perm = map(int, input().split())
prefix = [0] * (n + 1)

res = 'Yes'

for i in perm:
    if i > n or prefix[i] > 0:
        res = 'No'
        break
    prefix[i] = 1

print(res)