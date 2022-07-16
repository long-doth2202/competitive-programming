class Solution:
    def reverseWord(self, s: str) -> str:
        s_list = list(s)
        sz = len(s_list)

        for i in range(sz // 2):
            s_list[i], s_list[sz - i - 1] = s_list[sz - i - 1], s_list[i]

        return ''.join(s_list)

    def reverseWords(self, s: str) -> str:
        # return " ".join( [ i[::-1] for i in s.split() ])

        words = s.split(' ')
        sz = len(words)

        for i in range(sz):
            words[i] = self.reverseWord(words[i])
        
        return ' '.join(words)