from typing import List


class Solution:

    # brute force: time complexity O(n^2), space complexity O(1)
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    # two pointers technique: time complexity O(nlogn), space complexity O(1)
    def twoSumTwoPointers(self, nums: List[int], target: int) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] == target:
                return [nums[left][1], nums[right][1]]
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                right -= 1
        return []
    
    # two pass hash maps: time complexity O(n), space complexity O(n)
    def twoSumTwoPassHashMaps(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            hash_map[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map and i != hash_map[diff]:
                return [i, hash_map[diff]]
        return []

    # hash table: time complexity O(n), space complexity O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[num] = i
        return []
    