class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(list(s)) == Counter(list(t))
        map_s1 = [0 for i in range(30)]
        map_s2 = [0 for i in range(30)]

        n, m = len(s), len(t)

        for i in range(n):
            map_s1[ord(s[i]) - ord('a')] += 1
        for i in range(m):
            map_s2[ord(t[i]) - ord('a')] += 1

        return map_s1 == map_s2