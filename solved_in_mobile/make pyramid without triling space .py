num= int(input())
if 0<num<100:
	for i in range(0,num):
		for j in range(0,num-i-1):
			print(end=' ')
		for k in range(i+1):
			print('*',end= '')
			if k<i:
			 print(' ',end = '')
		print()
		
	
	