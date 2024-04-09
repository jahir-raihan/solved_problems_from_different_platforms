def count(n, a):
	count = 0 
	for i in range(len(n)):
		if n[i] == a:
			count += 1 
	return count

n = input() 
if len(n) > 1:
	 a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	 c = [] 
	 for i in range(len(a)):
	 	c.append(count(n, a[i]))
	 print(c.index(max(c)))
if len(n)==1:
	print(n)