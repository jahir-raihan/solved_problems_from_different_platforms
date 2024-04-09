def carry(A,B):
	for i in range(len(A)):
		if int(A[i])+int(B[i]) >9:
			return 'Yes'
	return 'No'
	
A,B =input().split()
if 0<int(A)<1000000 and 0<int(B)<1000000:
	if len(A)!=len(B):
		if len(A)>len(B):
			print(carry(B,A[::-1]))
		else:
			print(carry(A,B[::-1]))		
	else:
		print(carry(A,B))
	

	