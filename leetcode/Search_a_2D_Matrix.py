from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for i in matrix:
            if (i[0] <= target and i[-1] >= target):
                res += i
            else:
                break
        
        l, r = 0, len(res) - 1
        while l <= r:
            mid = (l + r) >> 1
            if res[mid] == target:
                return True
            elif res[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False