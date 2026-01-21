from typing import List

class Solution:

    # Optimized Deque Approach
    # Time Complexity: O(N), Space Complexity: O(K)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        deq = deque()
        max_indices = []

        for i in range(n):
            # Remove indices that are out of the current window
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove elements smaller than the current element from the deque
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            # Append the maximum for the current window to the results
            if i >= k - 1:
                max_indices.append(nums[deq[0]])

        return max_indices

    # Brute Force Approach
    # Time Complexity: O(N*K), Space Complexity: O(1)
    def maxSlidingWindowBruteForce(self, nums: List[int], k: int) -> List[int]:
        results = []
        n = len(nums)
        for i in range(n - k + 1):
            maximum = nums[i]
            for j in range(i, i + k):
                maximum = max(maximum, nums[j])
            results.append(maximum)
        return results