
import heapq
from typing import List

class Solution:

    # time complexity: O(n), space complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res 
        return res

    # time complexity: O(nlogn), space complexity: O(n)
    def topKFrequentWithSorting(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_count[:k]]
    
    # time complexity: O(nlogk), space complexity: O(n + k)
    def topKFrequentWithHeap(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _, num in heap]