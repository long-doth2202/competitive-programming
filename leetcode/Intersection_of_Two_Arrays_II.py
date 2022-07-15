from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = [] 
        for x in nums1: 
            if x in nums2: 
                nums2.remove(x) 
                nums3.append(x) 
        return nums3