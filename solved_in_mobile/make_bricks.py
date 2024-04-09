def make_bricks(small,big,goal):
	big = big*5
	if small+big == goal or big == goal or small== goal:
		return True
	if small>goal:
		return True
	if goal>big:
		have = small-(goal - big)		
		if have>0:
			return True
	if big>goal:		
		n = goal//5
		if n*5==goal:
			return True
		if goal>n*5:
			m = small-(goal-n*5)		
			if m>=0:
				return True
	return False		
	

make_bricks(1,4,11)