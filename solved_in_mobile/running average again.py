def avg(n,lst):
	num = 0
	for i in range(1,n+1):
		num+=lst[i-1]
		avg = num/i
		print(round(avg,10))
				
n = int(input())
lst = list(map(int,input().split()))
if n>0 and n<=100000 and max(lst)<1000 and min(lst)>0:
		avg(n,lst)
