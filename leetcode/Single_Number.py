class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda total, num: total ^ num, nums)

        sz = len(nums)
        ans = nums[0]

        for i in range(1, sz):
          ans = ans ^ nums[i]
        
        return ans