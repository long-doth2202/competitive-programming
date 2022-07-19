from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        vis = [[0 for i in range(n + 1)] for i in range(m + 1)]

        def inBoard(x, y):
            return (min(x, y) >= 0 and x < m and y < n)

        def bfs(x, y, fr, to):
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            queue = []
            queue.append([x, y])
            image[x][y] = to
            while (len(queue) != 0):
                top = queue.pop()
                x, y = top[0], top[1]
                # print(x, y)
                for i in range(4):
                    _x = x + dx[i]
                    _y = y + dy[i]
                    if (inBoard(_x, _y) and vis[_x][_y] == 0 and image[_x][_y] == fr):
                        image[_x][_y] = to
                        queue.append([_x, _y])
                        vis[_x][_y] = 1
            return image    
        
        return bfs(sr, sc, image[sr][sc], color)