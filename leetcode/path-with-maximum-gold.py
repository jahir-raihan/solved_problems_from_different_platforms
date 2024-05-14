def getMaximumGold(grid) -> int:
    max_sum = 0

    m, n = len(grid), len(grid[0])

    def get_max_sum(i, j, vis):

        cur_val = grid[i][j]

        q = []
        if i < m-1 and grid[i + 1][j] != 0 and (i + 1, j) not in vis:
            q.append((i + 1, j))
        if i > 0 and grid[i - 1][j] != 0 and (i - 1, j) not in vis:
            q.append((i - 1, j))
        if j < n-1 and grid[i][j + 1] != 0 and (i, j + 1) not in vis:
            q.append((i, j + 1))
        if j > 0 and grid[i][j - 1] != 0 and (i, j - 1) not in vis:
            q.append((i, j - 1))

        vis.add((i, j))

        local_max = 0
        for val in q:
            local_max = max(local_max, get_max_sum(val[0], val[1], vis))

        return cur_val + local_max

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:

                max_sum = max(max_sum, get_max_sum(i, j, set()))

    return max_sum


grid = [[1, 0, 7, 0, 0, 0],
       [2, 0, 6, 0, 1, 0],
       [3, 5, 6, 7, 4, 2],
       [4, 3, 1, 0, 2, 0],
       [3, 0, 5, 0, 20, 0]]

res = getMaximumGold(grid)

print(res)

