from typing import List

class Solution:

    # Time: O(n), Space: O(1)    
    def productExceptSelfOpt(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    # Time: O(n), Space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = [1] * n
        postfix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = prefix[i] * postfix[i]
        return res
    
    # Time: O(n^2), Space: O(1)
    def productExceptSelfBruteForce(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    res[i] *= nums[j]
        return res