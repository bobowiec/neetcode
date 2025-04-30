from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    res.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
        return [list(t) for t in res]
    
    # Time complexity: O(n^3), Space complexity: O(m); m - number of triplets
    def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        res.add(tuple(triplet))
        return [list(t) for t in res]