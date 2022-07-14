from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        sz = len(nums)
        k %= sz

        l, r = 0, sz - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        l, r = k, sz - 1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l + 1, r-1
        
        return nums