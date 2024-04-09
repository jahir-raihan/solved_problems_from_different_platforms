	
list = [1,2,2]
list1 = [1,2,1,2]
list3 = [1,1,2,1,1,1,1,2,1,2,1,2]
	

def has22(l):
		result =[]
		for i in range(len(l)):
			try:
				if l[i] ==2 and l[i+1]==2:
					result.append('found')
			except IndexError:
				pass
			else:
				result.append('Not found')	
		def retu():
				if 'found' in result:
					return True
				else:
					return False
	
		return retu()
					
has22(list1)




	