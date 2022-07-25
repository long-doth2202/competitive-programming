class Solution:
  def getHint(self, secret: str, guess: str) -> str:
    bulls = 0
    cows = 0
    pattern = "0123456789"
    s_dict, g_dict = {i: 0 for i in pattern}, {i: 0 for i in pattern}

    for i in range(len(secret)):
      if secret[i] == guess[i]:
        bulls += 1
      else:
        s_dict[secret[i]] += 1
        g_dict[guess[i]] += 1

    for i in pattern:
      cows += min(s_dict[i], g_dict[i])

    return f"{bulls}A{cows}B"