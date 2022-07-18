class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map_s1 = [0 for i in range(30)]
        map_s2 = [0 for i in range(30)]

        n, m = len(s1), len(s2)

        for i in range(n):
            map_s1[ord(s1[i]) - ord('a')] += 1
        
        # print(map_s1)

        j = 0
        map_s2[ord(s2[j]) - ord('a')] += 1
        if (map_s1 == map_s2):
            return True

        for i in range(1, m):
            order = ord(s2[i]) - ord('a') 
            map_s2[order] += 1
            if (map_s2[order] > map_s1[order]):
                while ord(s2[j]) - ord('a') != order and j < i:
                    map_s2[ord(s2[j]) - ord('a')] -= 1
                    j += 1
                
                map_s2[ord(s2[j]) - ord('a')] -= 1
                j += 1

            # print (j, i)
            if (map_s1 == map_s2):
                return True
            
        return False
