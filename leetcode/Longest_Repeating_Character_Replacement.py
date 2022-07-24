class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        mapped = {}
        sz = len(s)
        j = 0

        for i in range(sz):
            mapped[s[i]] = mapped.get(s[i], 0) + 1

            res = i - j + 1            
            if res - max(mapped.values()) <= k:
                ans = max(ans, res)
            else:
                mapped[s[j]] -= 1
                j += 1

        return ans