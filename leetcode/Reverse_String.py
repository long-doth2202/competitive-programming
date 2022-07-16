from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        sz = len(s)

        for i in range(sz // 2):
            s[i], s[sz - i - 1] = s[sz - i - 1], s[i]

        return s
        