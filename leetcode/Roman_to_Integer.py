class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for i, c in enumerate(s[:-1]):
            if nums[c] < nums[s[i + 1]]:
                res -= nums[c]
            else:
                res += nums[c]
        
        return res + nums[s[-1]]