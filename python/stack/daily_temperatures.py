from typing import List

class Solution:

    # O(n) time | O(n) space
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # indices of temperatures

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
    
    # O(n^2) time | O(1) space
    def dailyTemperaturesBruteForce(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res