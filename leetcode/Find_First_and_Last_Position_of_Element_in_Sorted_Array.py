from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.append((1<<31))
        
        l = bisect.bisect_left(nums, target)
        if l != len(nums) and nums[l] == target:
          ans.append(l)
        else:
          ans.append(-1)

        r = bisect.bisect_right(nums, target)
        if (r - 1) >= 0 and nums[r - 1] == target:
          ans.append(r)
        else:
          ans.append(-1)


        return ans