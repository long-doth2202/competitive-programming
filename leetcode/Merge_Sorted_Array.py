from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if (n == 0):
            return nums1
        if (m == 0):
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1

        j = m + n - 1
        for i in range(m - 1, -1, -1):
            nums1[j] = nums1[i]
            nums1[i] = 0
            j -= 1
        
        # print(nums1)

        k, i, j = 0, n, 0

        while i < m + n and j < n:
            # print(nums1)
            if (nums1[i] <= nums2[j]):
                nums1[k] = nums1[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                j += 1
        
        while (i < m + n):
            nums1[k] = nums1[i]
            i += 1
            k += 1

        while (j < n):
            nums1[k] = nums2[j]
            k += 1
            j += 1
        
        return nums1