from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = {}
        for i in range(0, len(nums)):
            if (arr[nums[i]] != 0):
                return True
            else:
                arr[nums[i]] += 1
        return False