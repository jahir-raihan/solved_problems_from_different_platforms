n = int(input())
a = map(int, input().split())
min_val = 999999999999

for i in a:
    min_val = min(min_val, abs(i))

print(min_val)