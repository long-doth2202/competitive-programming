from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        sz = len(nums)

        for i in range(sz):
            mapped[nums[i]] = i
        
        for i in range(sz):
            v = target - nums[i]
            print(nums[i], v)
            if (v not in mapped):
                continue
            else:
                if (mapped[v] != i):
                    return [i, mapped[v]]
