from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sz = len(nums)
        for i in range(1, sz):
            nums[i] += nums[i - 1]
        tmp, ans = 0, -(1 << 31)
        for i in range(sz):
            ans = max(ans, nums[i] - tmp)
            tmp = min(tmp, nums[i])
        return ans
