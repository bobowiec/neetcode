from typing import List

class Solution:

    # Time complexity: O(n), Space complexity O(1)
    def max_profit_two_pointer(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_p = 0

        while right < len(prices):
            if profit[left] < profit[right]:
                profit = profit[right] - profit[left]
                max_p = max(max_p, profit)
            else:
                left = right
            right += 1

        return max_p

    # Time complexity: O(n), Space complexity O(1)
    def max_profit_dynamic_programming(self, prices: List[int]) -> int:
        max_p = 0
        buy = prices[0]

        for sell in prices:
            max_p = max(max_p, sell - buy)
            buy = min(buy, sell)
            
        return max_p

    # Time complexity: O(n^2), Space complexity O(1)
    def max_profit_brute_force(self, prices: List[int]) -> int:
        n = len(prices)
        max_p = 0
        for i in range(n):
            buy = prices[i]
            for j in range(i + 1, n):
                sell = prices[j]
                max_p = max(max_p, sell - buy)
        return max_p