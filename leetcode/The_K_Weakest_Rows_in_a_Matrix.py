from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])

        rank = [[] for i in range(n + 1)]
        for i in range (m):
            cnt = 0
            for j in range(n):
                if (mat[i][j] == 1):
                    cnt += 1
            rank[cnt].append(i)
        ans = []
        for i in range(len(rank)):
            for j in range(len(rank[i])):
                if (k == 0):
                    return ans
                k -= 1
                ans.append(rank[i][j])
        return ans