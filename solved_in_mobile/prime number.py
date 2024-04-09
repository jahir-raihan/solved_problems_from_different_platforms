def is_prime(n):
	p,P = 'is not prime!','Prime'
	if n>1:
		for i in range(2,n):
			if (n%i)==0:
				print(p,f'\nBecause\n{i} × {n//i} = {n}')
				break
		else:
			print(P)
	elif n == 1:
		print(n,p,'\nAs we can say 1 is  a prime number beside not  a \nprime number ! To accomplish the prime number theory, \nwe choose 1 not as a prime number.  ')
	elif n==0:
		print(p,'\nBecause an integer that can only  divisible   by 1 and \nitself called an prime numeber.But 0 is not  divisible \nby 1,  That\'s why 0 is not a prime number.' )

def check_point(n):
	try:
		num = int(n)
	except Exception as e:
		print('Please enter an integer value!')
		print()
		check_point((input('Enter number to check: ')))
	else:
		n1 = int(n)
		if type(n1)==int:
			is_prime(n1)
			
			
check_point((input('Enter number to check:')))
		