def make_chocolate(small,big,goal):
	if (small+big*5)<goal:
		return -1
	elif (big*5)>goal:
		n = goal%5
		if n>small:
			return -1
		return goal%5
	else:
		return goal-big*5
	
make_chocolate(1,2,7)