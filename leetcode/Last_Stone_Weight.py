from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
          stones[i] = -stones[i]
        heapq.heapify(stones)
        while (True): 
          if (len(stones) == 1): 
            return -stones[0]
          x = -heapq.heappop(stones)
          y = -heapq.heappop(stones)
          z = x - y
          heapq.heappush(stones, -z)
        