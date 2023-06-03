
for _ in range(int(input())):
  n, k = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  a = [(a[i],i) for i in range(n)]
  a.sort()
  b.sort()
  o=[0]*n
  for i in range(n):
    v,j=a[i]
    o[j]=b[i]
  print(*o)