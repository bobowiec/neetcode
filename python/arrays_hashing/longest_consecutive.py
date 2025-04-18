from typing import List

class Solution:

    # Time complexity: O(n), Space complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            # check if n is the start of sequence
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest

    # Time complexity: O(n*log(N)), Space complexity: O(n)
    def longestConsecutiveWithSorting(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_set = sorted(set(nums))

        longest = 1
        curr = 1
        for i in range(len(sorted_set) - 1):
            if sorted_set[i] == sorted_set[i+1] - 1:
                curr += 1
            else:
                curr = 1
            longest = max(curr, longest)
        return longest

    # Time complexity: O(n^2), Space complexity: O(n)
    def longestConsecutiveBruteForce(self, nums: List[int]) -> int:
        res = 0
        hash_set = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in hash_set:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res