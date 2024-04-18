class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        k = len(grid[0])

        res = 0
        for i in range(n):
            for j in range(k):
                if grid[i][j] == 1:
                    sides = 0

                    if i == 0 or grid[i - 1][j] == 0:
                        sides += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        sides += 1
                    if i == n - 1 or grid[i + 1][j] == 0:
                        sides += 1
                    if j == k - 1 or grid[i][j + 1] == 0:
                        sides += 1

                    res += sides
        return res
