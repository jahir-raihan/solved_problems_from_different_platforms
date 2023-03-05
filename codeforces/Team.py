res = 0
for _ in range(int(input())):
    s = input().count('1')
    if s > 1:
        res += 1
print(res)
