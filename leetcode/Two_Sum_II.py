from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapped = {}
        sz = len(numbers)

        for i in range(sz):
            mapped[numbers[i]] = i
        
        for i in range(sz):
            v = target - numbers[i]
            # print(numbers[i], v)
            if (v not in mapped):
                continue
            else:
                if (mapped[v] != i):
                    return [i + 1, mapped[v] + 1]