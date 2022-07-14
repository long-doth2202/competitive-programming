class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sz_s, sz_t = len(s), len(t)
        dp = [[0 for x in range(sz_t + 5)] for y in range(sz_s + 5)]
        s = " " + s
        t = " " + t

        for i in range(1, sz_s + 1):
            for j in range(1, sz_t + 1):
                if (s[i] == t[j]):
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j], max(dp[i][j - 1], dp[i - 1][j]))
        
        ans = 0
        for i in range(1, sz_s + 1):
            for j in range(1, sz_t + 1):
                ans = max(ans, dp[i][j])
        
        return ans == sz_s