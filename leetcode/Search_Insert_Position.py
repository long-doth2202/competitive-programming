from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right, mid, ans = 0, len(nums) - 1, 0, len(nums)
        while (left <= right):
            mid = (left + right) >> 1
            if (nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans        