from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        ans = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r * c):
            ans[i // c][i % c] = mat[i // n][i % n]

        return ans         