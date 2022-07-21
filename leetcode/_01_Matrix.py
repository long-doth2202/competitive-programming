from typing import List
import queue

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        ans = [[0 for i in range(n)] for i in range(m)]

        def inBoard(x, y):
            return min(x, y) >= 0 and x < m and y < n

        q = queue.Queue()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.put([i, j])

        while q.empty() == False:
            cell = q.get()
            for i in range(4):
                x = cell[0] + dx[i]
                y = cell[1] + dy[i]
                if inBoard(x, y) and mat[x][y] != 0:
                    mat[x][y] = 0
                    ans[x][y] = ans[cell[0]][cell[1]] + 1
                    q.put([x, y])
        
        return ans