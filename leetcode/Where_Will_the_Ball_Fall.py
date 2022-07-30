class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
      m, n = len(grid), len(grid[0])
      ans = []

      def drop(col):
        for row in range(m):
          col_next = col + grid[row][col]
          if col_next < 0 or col_next >= n or grid[row][col_next] != grid[row][col]:
            return -1
          col = col_next
        
        return col
      
      for col in range(n):
        ans.append(drop(col))