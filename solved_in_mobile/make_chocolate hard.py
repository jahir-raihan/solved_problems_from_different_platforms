def make_chocolate(small,big,goal):
	big = big*5
	if big==goal:
		return big-goal
		
	if small+big == goal or small== goal:
		return small
		
	if small>goal:
		n = small-goal
		n1= small-n
		return n1
	if goal>big:
		have = small-(goal - big)		
		if have>=0:
			return  small-have
		return -1
	if big>goal:		
		n = goal//5
		if n*5==goal:
			return  0
		if goal>n*5:
			m = small-(goal-n*5)
			if m>=0:
				mm = small-m
				if mm>=0:
					return mm
	return -1		
	

make_chocolate(1,2,6)