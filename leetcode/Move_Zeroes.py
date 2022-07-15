from typing import List 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a, b = 0, 1
        sz = len(nums)
        while a < sz and b < sz:
            if (nums[a] == 0 and nums[b] == 0):
                b += 1
            elif (nums[a] == 0 and nums[b] != 0):
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
            else:
                a += 1
                b += 1

        return nums