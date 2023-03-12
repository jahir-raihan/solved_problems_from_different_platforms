grid = [["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]

h = len(grid)
w = len(grid[0])
v = {}

cnt = 0

for i in range(h):
    for j in range(w):
        if grid[i][j] == '1' and f'{i},{j}' not in v:
            q = [(i, j)]

            while q:
                loc = q.pop()
                l, r = loc[0], loc[1]
                if f'{l},{r}' not in v:
                    v[f'{l},{r}'] = 1
                    if r < w - 1 and grid[l][r + 1] == '1' and f'{l},{r+1}' not in v:
                        q.append((l, r + 1))
                    if l < h - 1 and grid[l + 1][r] == '1' and f'{l+1},{r}' not in v:
                        q.append((l+1, r))
                    if r > 0 and grid[l][r - 1] == '1' and f'{l},{r-1}' not in v:
                        q.append((l, r - 1))
                    if l > 0 and grid[l - 1][r] == '1' and f'{l-1},{r}' not in v:
                        q.append((l - 1, r))
            cnt += 1


print(cnt)

