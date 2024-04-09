
def sum13(num):
	if 13 in num :
		
		if num.index(13)==0:
			del num[0:2]
			
		if 13 in num:
			del num[num.index(13):num.index(13)+2]
			
		sum13(num)
		
	return sum(num)
	
print(sum13([13, 1, 2, 13, 2, 1, 13]))