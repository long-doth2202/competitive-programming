class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapped = [0 for i in range(300)]
        sz = len(s)

        if (sz == 0):
            return 0

        ans, j = 1, 0
        mapped[ord(s[j])] = 1

        for i in range(1, sz):
            order = ord(s[i])
            
            mapped[order] += 1
            if (mapped[order] == 1):
                pass
            else:
                while ord(s[j]) != order and j < i:
                    mapped[ord(s[j])] -= 1
                    j += 1
                
                mapped[ord(s[j])] -= 1
                j += 1

            ans = max(ans, i - j + 1)
            
        return ans
            