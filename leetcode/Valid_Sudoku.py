from typing import List
 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSub(x, y):
            mapped = {}
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if (board[i][j] == '.'):
                        continue
                    if (board[i][j] not in mapped):
                        mapped[board[i][j]] = True
                    else:
                        return False
            return True
        
        def checkRow(row):
            mapped = {}
            for j in range(9):
                if (board[row][j] == '.'):
                        continue
                if (board[row][j] not in mapped):
                    mapped[board[row][j]] = True
                else:
                    return False
            return True

        def checkCol(col):
            mapped = {}
            for i in range(9):
                if (board[i][col] == '.'):
                        continue
                if (board[i][col] not in mapped):
                    mapped[board[i][col]] = True
                else:
                    return False
            return True
                    
        
        m, n = 9, 9
        for i in range(0, m - 2, 3):
            for j in range(0, n - 2, 3):
                if (checkSub(i, j) == False):
                    return False

        for i in range(m):
            if checkCol(i) == False:
                return False
            if checkRow(i) == False:
                return False

        return True