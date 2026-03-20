class Solution:

    # Time complexity: O(logn), Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            # left side is ordered
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right side is ordered
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return - 1

    # Time complexity: O(n), Space Complexity: O(1)
    def searchBruteForce(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1     
