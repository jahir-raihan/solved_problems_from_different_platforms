n = int(input())
a = [int(i) for i in input().split()]
x = int(input())

cnt = n
tot_sum = sum(a)
res = tot_sum
while res <= x:
  res += tot_sum
  cnt += n
i = n - 1
while res > x:
  res -= a[i]
  cnt -= 1
  i -= 1
print(cnt + 1)