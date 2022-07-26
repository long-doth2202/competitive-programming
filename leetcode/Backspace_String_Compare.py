class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sts = []
        stt = []
        m, n = len(s), len(t)

        for i in range(m):
          if (s[i] == '#'):
            if len(sts) != 0:
              sts.pop()
          else:
            sts.append(s[i])

        for i in range(n):
          if (t[i] == '#'):
            if len(stt) != 0:
              stt.pop()
          else:
            stt.append(t[i])

        return (' '.join(sts) == ' '.join(stt))
        