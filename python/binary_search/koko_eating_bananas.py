class Solution:

    # m -> max(piles), n -> len(piles)
    # Time complexity: O(log(m) * n), Space complexity: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2

            total_time = 0
            for pile in piles:
                #total_time += math.ceil(pile / k)
                total_time += (pile + k - 1) // k
            
            if total_time <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res

    # m -> max(piles), n -> len(piles) 
    # Time complexity: O(m * n), Space complexity: O(1)
    def minEatingSpeedBruteForce(self, piles: List[int], h: int) -> int:
        max_val = max(piles)

        for k in range(1, max_val + 1):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                return k
        return max_val
