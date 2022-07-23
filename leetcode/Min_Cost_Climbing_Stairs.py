from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        dp = [1000 ** 2 for i in range(n + 5)]

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i], min(dp[i - 1] + cost[i], dp[i - 2] + cost[i]))
        
        return dp[n - 1]
        