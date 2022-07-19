class Solution:
    def numberOfSteps(self, num: int) -> int:
        # return len(bin(num)[2:]) + bin(num).count('1') - 1
        steps = 0 
        
        while num:
            if num % 2:
                num -= 1
                steps += 1
            else:
                num /= 2
                steps += 1
                
        return steps