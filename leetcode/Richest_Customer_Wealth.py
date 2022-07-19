class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            _sum = sum(i)
            ans = max(ans, _sum)
        
        return ans