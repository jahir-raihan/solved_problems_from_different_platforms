intervals = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]

intervals.sort()
res = 0

cur_interval = intervals[0]

for i in range(1, len(intervals)):
    if intervals[i][0] <= cur_interval[1]:
        cur_interval[1] = min(cur_interval[1], intervals[i][1])
    else:
        res += 1
        cur_interval = intervals[i]

res += 1
print(res)