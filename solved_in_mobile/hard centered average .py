
def centered_average(l):
	def result(l):
		n = len(l)//2		
		return l[n]
		
	def result1(l):
		n, l1= len(l)//2-1,[]
		for i in range(abs(l[n]),abs(l[n+1])+1):
				if l[n]<0:
					l1.append(-i)
				if l[n]>0:
					l1.append(i)
				
		if len(l1)==2:
			return l1[1]
		n = len(l1)//2
		return l1[n]			
					
	def is_odd(l):
		if len(l)%2!=0:
			return True
		return False
		
	if is_odd(l):
		return result(l)
	if not is_odd(l) :
		return result1(l)
		
				
centered_average([-10,-4,-2,-4,-2,-10])
