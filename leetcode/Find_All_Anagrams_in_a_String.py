from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        ans = []

        map_p = [0 for i in range(27)]
        map_s = [[0 for i in range(27)] for i in range(m + 5)]

        for i in range(n):
            map_p[ord(p[i]) - ord('a')] += 1
        for i in range(m):
            if i > 0:
                for j in range(27):
                    map_s[i][j] = map_s[i - 1][j]
            map_s[i][ord(s[i]) - ord('a')] += 1

        for i in range(n - 1, m):
            j = i - n
            sum_prev = [0 for i in range(27)]
            if j >= 0:
                sum_prev = map_s[j]
            
            match = True
            for x in range(27):
                if map_s[i][x] - sum_prev[x] != map_p[x]:
                    match = False
            
            if match:
                ans.append(i - n + 1)

        return ans