class Solution:
    def isValid(self, s: str) -> bool:
        map_brackets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c not in stack:
                stack.append(c)
            else:
                if stack:
                    last = stack.pop()
                    if last != map_brackets[c]:
                        return False
                else:
                    return False
        
        return False if stack else True