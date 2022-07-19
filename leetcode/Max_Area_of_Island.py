from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        m, n = len(grid), len(grid[0])
        vis = [[0 for i in range(n + 1)] for i in range(m + 1)]
        num = [0]
        ans = 0

        def inBoard(x, y):
            return (min(x, y) >= 0 and x < m and y < n)

        def dfs(x, y, num):
            grid[x][y] = 0
            num[0] += 1
            for i in range(4):
                _x = x + dx[i]
                _y = y + dy[i]
                if (inBoard(_x, _y) == True and grid[_x][_y] == 1):
                    dfs(_x, _y, num)

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    num = [0]
                    dfs(i, j, num)
                    ans = max(ans, num[0])
        
        return ans