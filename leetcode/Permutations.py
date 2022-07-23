from itertools import permutations
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permute = permutations(nums)
        ans = []
        for i in list(permute):
            ans.append(list(i))
        return ans