from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        global ans
        ans = []
        global n
        n = len(s)

        def generateString(s_gen, m):
            if (m == n):
                ans.append(s_gen)
                return
            t = ""
            for i in range(m):
                t += s_gen[i]
            if (s[m].isalpha() == False):
                t += s[m]
                generateString(t, m + 1)
            else:
                generateString(t + s[m].upper(), m + 1)
                generateString(t + s[m].lower(), m + 1)

        generateString("", 0)
        return ans