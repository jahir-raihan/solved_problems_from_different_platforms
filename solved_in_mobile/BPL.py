def bpl(s):
	count = 0
	for i in range(len(s)):
		if s[i]!='N' and s[i]!='W' and s[i]!='D':
			count+=1
	ball = count%6
	over = count//6
	if ball==0 and over!=0:
		print(over,('OVERS' if over>1 else 'OVER'))
	elif over == 0 and ball!=0:
		print(ball,('BALLS' if ball>1 else 'BALL'))
	else:
		print(over,('OVERS' if over>2 else 'OVER'),ball,('BALLS' if ball>1 else 'BALL'))
	
T = int(input())
for i in range(T):
	s = input()
	bpl(s)
		

	
	