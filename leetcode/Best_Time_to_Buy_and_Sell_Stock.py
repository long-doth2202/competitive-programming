from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_profit = (1 << 31), -(1 << 31)
        sz = len(prices)

        for i in range(sz):
            min_buy = min(min_buy, prices[i])
            max_profit = max(max_profit, prices[i] - min_buy) 

        return max_profit       