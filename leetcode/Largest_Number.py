  from typing import List
  import functools

  def comp(s1, s2):
    if int(s1+s2) < int(s2+s1):
      return -1
    if int(s1+s2) > int(s2+s1):
      return 1
    return 0

  class Solution:
    def largestNumber(self, nums: List[int]) -> str:  
      nums = [str(num) for num in nums]
      nums = sorted(nums, key = functools.cmp_to_key(comp), reverse = True)
      ans = "0" if nums[0] == '0' else ''.join(nums)
      return ans