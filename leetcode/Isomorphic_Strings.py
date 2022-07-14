from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapped = {}
        sz = len(s)
        for i in range(sz):
            if ((s[i] in mapped) == False):
                mapped[s[i]] = t[i]
            else:
                if (mapped.get(s[i]) != t[i]):
                    return False
        
        mapped.clear()
        s, t = t, s

        for i in range(sz):
            if ((s[i] in mapped) == False):
                mapped[s[i]] = t[i]
            else:
                if (mapped.get(s[i]) != t[i]):
                    return False
        
        return True