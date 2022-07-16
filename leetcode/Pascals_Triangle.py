from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # return [[math.factorial(n) // math.factorial(n - k) // math.factorial(k) for k in range(n+1)] for n in range(numRows)]        
        result = [[1], [1, 1]]
        add_on = [1]
        if numRows == 1:
            return [[1]]
        else:
            for j in range(1, numRows - 1):
                add_on = [1]
                for i in range(len(result) - 1):
                    add_on.append(result[j][i] + result[j][i + 1]) 
                add_on.append(1)
                result.append(add_on)
            return result