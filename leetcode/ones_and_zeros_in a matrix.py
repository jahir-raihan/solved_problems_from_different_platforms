grid = [[1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0]]
h = len(grid)
w = len(grid[0])
diff = [[0 for i in range(w)] for j in range(h)]


def get_col(i,v):
    cnt = 0
    for n in range(h):
        if grid[n][i] == v:
            cnt += 1
    return cnt


memo = {}

for i in range(h):
    for j in range(w):

        try:
            val = memo[f'{i},{j}']
            col_1 = val[0]
            col_0 = val[1]
        except:
            memo[f'{i},{j}'] = [get_col(j, 1), get_col(j, 0)]
            val = memo[f'{i},{j}']
            col_1 = val[0]
            col_0 = val[1]
        try:
            row1 = memo[i][0]
            row0 = memo[i][1]
        except:
            memo[i] = [grid[i].count(1), grid[i].count(0)]
            row1 = memo[i][0]
            row0 = memo[i][1]

        diff[i][j] = row1 + col_1 - row0 - col_0
print(diff)