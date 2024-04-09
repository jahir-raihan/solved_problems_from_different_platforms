def sum67(l):
		if 6 in l:
			def remove(l):
				index1,index2 =l.index(6),l.index(7,l.index(6))
				del l[index1:index2+1]
			remove(l)					
		return sum(l)
		
sum67([2,7,6, 2, 6, 7, 2, 7])

	

