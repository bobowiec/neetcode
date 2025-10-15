from typing import List

class Solution:

    # Time complexity: O(n), Space complexity O(1)
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        res = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res
    
    # Time complexity: O(n), Space complexity O(n)
    def trap_with_prefix_suffix_sums(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        left_max = [0] * n
        right_max = [0] * n

        left_max = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        right_max = height[n-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
    
    # Time complexity: O(n^2), Space complexity O(1)
    def trap_brute_force(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        res = 0
        for i in range(n):
            left_max = right_max = height[i]

            for j in range(i):
                left_max = max(left_max, height[j])
            
            for j in range(i+1, n):
                right_max = max(right_max, height[j])
            
            res += min(left_max, right_max) - height[i]
        return res