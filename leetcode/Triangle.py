from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[0])

        dp = [[(1 << 31) for i in range(j + 5)] for j in range(m + 5)]

        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + triangle[i][j])
                if (j > 0):
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + triangle[i][j])

        ans = (1 << 31)

        for i in range(len(triangle[m - 1])):
            ans = min(ans, dp[m - 1][i])
        return ans
        # print(dp)