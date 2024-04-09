def count(n,a):
	count = 0
	for i in range(len(n)):
		if n[i]==a:
			count+=1
	return count
					
n=int(input())
n = str(n)
if len(n)>1 and len(n)<10**10000:
	a = '1234567890'
	c = ''
	for i in range(len(a)):
		c+=str(count(n,a[i]))
	print(c.index(max(c))+1)
	
