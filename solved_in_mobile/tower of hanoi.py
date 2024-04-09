A, B,C= [],[],[]
def showall():
	print(A,B,C,'___________',sep='\n')
	
def move(n,source,terget,bridge):
	if n>0:
		move(n-1,source,bridge,terget)
		terget.append(source.pop())
		showall()
		move(n-1,bridge,terget,source)
		

		
discs = int(input('enter discs: '))
A = list(range(1,discs+1))[::-1]
showall()
move(discs,A,B,C)
print('number of moves :',str(2**discs-1))