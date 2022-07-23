from itertools import combinations
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = combinations([i for i in range(1, n + 1)], k)
        ans = []
        for i in list(comb):
            ans.append(list(i))
        return ans