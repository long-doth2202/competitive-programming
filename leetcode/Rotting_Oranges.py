from typing import List
import queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        dist = [[0 for i in range(n)] for i in range(m)]

        def inBoard(x, y):
            return min(x, y) >= 0 and x < m and y < n
        
        q = queue.Queue()
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 2):
                    q.put([i, j])

        while q.empty() == False:
            cell = q.get()
            for i in range(4):
                x = cell[0] + dx[i]
                y = cell[1] + dy[i]
                if inBoard(x, y) and grid[x][y] == 1 and dist[x][y] == 0:
                    dist[x][y] = dist[cell[0]][cell[1]] + 1
                    q.put([x, y])
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if dist[i][j] == 0 and grid[i][j] == 1:
                    return -1
                ans = max(ans, dist[i][j])
        
        return ans