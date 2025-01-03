from typing import List

class Solution:

    # brute force: time complexity O(n^2), space complexity O(1)
    def hasDuplicateBruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    # hash set: time complexity O(n), space complexity O(n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False
