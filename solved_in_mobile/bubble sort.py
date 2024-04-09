def bubble_sort(num):
	for i in range(len(num)):
		for j in range(0,len(num)-i-1):
			if num[j]>num[j+1]:
				num[j],num[j+1]=num[j+1],num[j]
	return num
		
	
num = [3,4,9,6,1,2]
print(bubble_sort(num))