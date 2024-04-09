main = "3[abc]4[ab]7[acb]9[abcd]7[efgh]e"

num,numbers = [],'1234567890'

def sp(main):
	
	global other
	other = ''
	
	for i in main:
		if i in numbers:
			num.append(i)
		else:
			other += i
			
sp(main)		
nums = list(map(int,num))

def remove_bracket(string):
	import re
#	main = '[abc][ab][cd]c'
	pattern = '\[.*?\]'
	
	match = re.findall(pattern,string)
	decom =[]
	
	for i in match:
		
		r1 = i.replace('[','')
		
		r2 = r1.replace(']','')
		
		decom.append(r2)
		
	return decom

str1 = remove_bracket(other)

print(nums)
print(other)

def mul(nums,string):	
	return nums*string
	
last = ''

for i in range(len(nums)):
	last +=mul(nums[i],str1[i])

print(last+other[-1])
	
