class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapped = [0 for i in range(30)]

        sz = len(s)
        
        for i in range(sz):
            mapped[ord(s[i]) - ord('a')] += 1

        for i in range(sz):
            if mapped[ord(s[i]) - ord('a')] == 1:
                return i

        return -1