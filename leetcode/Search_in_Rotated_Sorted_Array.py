class Solution:
    def search(self, nums: List[int], target: int) -> int:
      left, right = 0, len(nums)
      while left < right:
        mid = (left + right) >> 1
        if target < nums[0] < nums[mid]: # -inf
          left = mid + 1
        elif target >= nums[0] > nums[mid]: # inf
          right = mid
        elif nums[mid] < target:
          left = mid + 1
        elif nums[mid] > target:
          right = mid
        else:
          return mid
      
      
      return -1