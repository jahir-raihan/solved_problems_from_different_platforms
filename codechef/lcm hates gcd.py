import math
t = int(input())
for i in range(t):
	a,b = map(int,input().split())
	x = math.gcd(a,b)

	print(a-x)