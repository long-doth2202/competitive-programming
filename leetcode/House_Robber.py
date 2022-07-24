class Solution:
    def rob(self, nums: List[int]) -> int:
        sz = len(nums)
        dp = [0 for i in range(sz + 5)]

        if (sz == 1): return nums[0]
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        ans = max(nums[0], nums[1])

        for i in range(2, sz):
            for j in range(0, i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
            ans = max(ans, dp[i])
        return ans