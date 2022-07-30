class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
      sz = len(nums)
      if sz == 1: return 0
      if nums[0] > nums[1]: return 0
      if nums[sz - 1] > nums[sz - 2]: return sz - 1
      left, right, mid, ans = 1, len(nums) - 1, 0, -1

      while left <= right:
        mid = (left + right) >> 1
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
          ans = mid
          break
        elif nums[mid] < nums[mid - 1]:
          right = mid - 1
        else:
          left = mid + 1
      
      return ans  