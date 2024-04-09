def close_far(a,b,c):
	condition = abs(a-b)<=1 and abs(b-c)>=2 and abs(a-c)>=2
	condition1 = abs(a-c)<=1 and abs(a-b)>=2 and abs(b-c)>=2
	return condition or condition1
close_far(10,10,8)