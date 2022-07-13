from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i, x in enumerate(nums):
            if (leftSum == totalSum - leftSum - x):
                return i 
            leftSum += x
        return -1