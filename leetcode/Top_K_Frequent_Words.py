import collections
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      # return [word[0] for word in Counter(sorted(words)).most_common(k)]
        c = collections.Counter()
        for word in words:
          c[word] += 1
        
        w_freq = c.most_common()
        w_freq.sort(key = lambda x: x[0])
        w_freq.sort(key = lambda x: x[1], reverse = True)
        res = [word[0] for word in w_freq]
        return res[:k]