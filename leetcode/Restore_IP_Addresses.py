from typing import List
import itertools

def valid_part(part):
  return ((not (part[0] == '0' and part != "0")) and int(part) <= 255)

def valid_ip(parts):
  return all(valid_part(part) for part in parts)

class Solution:
  def restoreIpAddresses(self, s: str) -> List[str]:  
    res = []
    for i, j, k in itertools.combinations(range(1, len(s)), 3):
      parts = [s[:i], s[i:j], s[j:k], s[k:]]
      if (valid_ip(parts)):
        res.append('.'.join(parts))
    return res