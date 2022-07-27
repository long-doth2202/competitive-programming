class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sz = len(nums)
        ans, cnt = nums[0], 1

        for i in range(1, sz):
          if cnt == 0:
            ans = nums[i]
            cnt = 1
          elif nums[i] == ans:
            cnt += 1
          else:
            cnt -= 1
        
        return ans