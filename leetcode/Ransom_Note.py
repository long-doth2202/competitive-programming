class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_s1 = [0 for i in range(30)]
        map_s2 = [0 for i in range(30)]

        n, m = len(ransomNote), len(magazine)

        for i in range(n):
            map_s1[ord(ransomNote[i]) - ord('a')] += 1
        for i in range(m):
            map_s2[ord(magazine[i]) - ord('a')] += 1

        for i in range(0, 27):
            if (map_s1[i] > map_s2[i]):
                return False
        
        return True