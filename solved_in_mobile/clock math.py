
def clock_math(H,M):
	if H == 12 and M == 00:
		print(0)
	res =(11*M-60*H)/2
	if abs(res)>=180:
		print(round(360-abs(res),10))
	else:
		print(round(abs(res),10))
	
H,M = map(int,input().split())
clock_math(H,M)
	
