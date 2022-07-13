from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, mid, ans = 0, len(nums) - 1, 0, -1
        while left <= right:
            mid = (left + right) >> 1
            if (nums[mid] == target):
                ans = mid
                break
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return ans