class Solution:

    # Time complexity: O(logn), Space complexity: O(1)
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break

            mid = (left + right) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res
    
    # Time complexity: O(logn), Space complexity: O(1)
    def findMinBinarySearchLowerBound(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

    # Time complexity: O(n), Space complexity: O(1)
    def findMinBruteForce(self, nums: List[int]) -> int:
        return min(nums)
        
