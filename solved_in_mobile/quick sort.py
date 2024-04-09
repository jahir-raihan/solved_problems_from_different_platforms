def quick_sort(num):
	if num==[]:
		return []
	else:
		x, *xs=  num
		smaller = quick_sort([a for a in xs if a<=x])
		bigger = quick_sort([b for b in xs if b>x])
		res = smaller+[x]+bigger
		return res
	
print(quick_sort([9,8,7,6,5,3,3,2,1]))