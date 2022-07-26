class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            
            if s[i] == ']':
                sub = ''
                while stack[-1] != '[':
                    sub += stack.pop()
                stack.pop() 
                mult = int(stack.pop())
                sub *= mult
                for j in range(len(sub)-1,-1,-1): 
                    stack.append(sub[j]) 
                i += 1
            else:
                if s[i].isdigit():
                    num = ''
                    while s[i].isdigit():
                        num += s[i]
                        i += 1
                    stack.append(num)
                else:
                    stack.append(s[i])
                    i += 1
        return ''.join(stack)