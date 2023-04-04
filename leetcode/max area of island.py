grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]

max_area = 0
v = {}


def ck_v_h(x, y):
    if x > 0 and grid[x-1][y] == 1 and (x-1,y) not in q:
        try:v[f'{x-1},{y}']
        except:q.append((x-1, y))
    if x < len(grid) - 1 and grid[x+1][y] == 1 and (x+1,y) not in q:
        try:v[f'{x+1},{y}']
        except:q.append((x+1, y))
    if y > 0 and grid[x][y - 1] == 1 and (x,y-1) not in q :
        try:v[f'{x},{y-1}']
        except:q.append((x, y - 1))
    if y < len(grid[0]) - 1 and grid[x][y + 1] == 1 and (x,y+1) not in q:
        try:v[f'{x},{y+1}']
        except:q.append((x, y + 1))


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1 and f'{i},{j}' not in v:
            q = [(i,j)]
            cnt = 0
            while q:
                tmp = q.pop()
                cnt += 1
                v[f'{tmp[0]},{tmp[1]}'] = 1
                ck_v_h(tmp[0], tmp[1])
            max_area = max(cnt, max_area)
print(max_area)


