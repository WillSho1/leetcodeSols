from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0]*len(temperatures)

        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][1]:
                index = stack.pop()[0]
                days[index] = i - index
            stack.append((i, temp))

        return days